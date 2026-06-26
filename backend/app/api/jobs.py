from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.models import Job, Application
from app.api.auth import get_current_user
from app.models import User
from app.agents.enhanced_agents import JobSearchAgent
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

job_search_agent = JobSearchAgent()

@router.get("/search")
async def search_jobs(
    q: str,
    location: str = None,
    salary_min: float = None,
    salary_max: float = None,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Search for jobs"""
    try:
        jobs = await job_search_agent.search_jobs(
            query=q,
            location=location,
            salary_min=salary_min,
            salary_max=salary_max,
            user_id=current_user.id
        )
        
        return {
            "query": q,
            "total": len(jobs),
            "jobs": jobs
        }
    except Exception as e:
        logger.error(f"Job search error: {e}")
        raise HTTPException(status_code=500, detail="Failed to search jobs")

@router.get("/saved")
async def get_saved_jobs(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get user's saved jobs"""
    saved_jobs = db.query(Job).filter(
        Job.user_id == current_user.id,
        Job.is_saved == True
    ).all()
    
    return {"saved_jobs": saved_jobs}

@router.post("/{job_id}/save")
async def save_job(
    job_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Save job for later"""
    job = db.query(Job).filter(Job.id == job_id).first()
    
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    job.is_saved = True
    db.commit()
    
    logger.info(f"Job {job_id} saved by user {current_user.id}")
    
    return {"message": "Job saved successfully"}

@router.post("/match")
async def match_jobs(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Match jobs based on user profile"""
    # Get user's resume
    from app.models import Resume
    resume = db.query(Resume).filter(
        Resume.user_id == current_user.id,
        Resume.is_primary == True
    ).first()
    
    if not resume:
        raise HTTPException(status_code=400, detail="No primary resume found")
    
    # Get matched jobs
    matched_jobs = []
    
    return {
        "total_matches": len(matched_jobs),
        "matches": matched_jobs
    }
