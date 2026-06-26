from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models import Application
from app.api.auth import get_current_user
from app.models import User
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/")
async def list_applications(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """List user's applications"""
    applications = db.query(Application).filter(
        Application.user_id == current_user.id
    ).all()
    
    return {"applications": applications}

@router.post("/")
async def create_application(
    job_id: int,
    resume_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create new application"""
    application = Application(
        user_id=current_user.id,
        job_id=job_id,
        resume_id=resume_id,
        status="applied"
    )
    
    db.add(application)
    db.commit()
    
    logger.info(f"Application created for user {current_user.id}")
    
    return {"id": application.id, "message": "Application created"}

@router.put("/{application_id}/status")
async def update_application_status(
    application_id: int,
    status: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Update application status"""
    application = db.query(Application).filter(
        Application.id == application_id,
        Application.user_id == current_user.id
    ).first()
    
    if not application:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Application not found")
    
    application.status = status
    db.commit()
    
    return {"message": "Status updated"}
