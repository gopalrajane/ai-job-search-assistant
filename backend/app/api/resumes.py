from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models import Resume, User
from app.api.auth import get_current_user
from app.agents.enhanced_agents import ResumeAnalysisAgent
import logging
import os
from pathlib import Path

logger = logging.getLogger(__name__)
router = APIRouter()

resume_agent = ResumeAnalysisAgent()

@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Upload and parse resume"""
    try:
        # Validate file
        allowed_types = ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]
        if file.content_type not in allowed_types:
            raise HTTPException(status_code=400, detail="Only PDF and DOCX files allowed")
        
        # Save file
        upload_dir = Path("uploads")
        upload_dir.mkdir(exist_ok=True)
        
        file_path = upload_dir / f"{current_user.id}_{file.filename}"
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Parse resume
        extracted_data = await resume_agent.analyze_resume(str(file_path))
        
        # Save to database
        resume = Resume(
            user_id=current_user.id,
            filename=file.filename,
            file_path=str(file_path),
            file_size=len(content),
            extracted_text="",
            skills=extracted_data.get("skills", []),
            experience=extracted_data.get("experience", []),
            education=extracted_data.get("education", []),
            projects=extracted_data.get("projects", []),
            summary=extracted_data.get("summary", "")
        )
        
        db.add(resume)
        db.commit()
        
        logger.info(f"Resume uploaded for user {current_user.id}")
        
        return {
            "id": resume.id,
            "filename": resume.filename,
            "extracted_data": extracted_data
        }
    
    except Exception as e:
        logger.error(f"Resume upload error: {e}")
        raise HTTPException(status_code=500, detail="Failed to upload resume")

@router.get("/")
async def list_resumes(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List user's resumes"""
    resumes = db.query(Resume).filter(Resume.user_id == current_user.id).all()
    return {"resumes": resumes}

@router.get("/{resume_id}")
async def get_resume(
    resume_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get resume details"""
    resume = db.query(Resume).filter(
        Resume.id == resume_id,
        Resume.user_id == current_user.id
    ).first()
    
    if not resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    
    return resume
