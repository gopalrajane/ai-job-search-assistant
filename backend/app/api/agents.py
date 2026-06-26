from fastapi import APIRouter

router = APIRouter()

@router.post("/orchestrator")
async def call_orchestrator():
    return {"message": "Orchestrator called"}

@router.post("/job-search")
async def call_job_search():
    return {"message": "Job search agent called"}

@router.post("/resume-analysis")
async def call_resume_analysis():
    return {"message": "Resume analysis agent called"}

@router.post("/ats-scoring")
async def call_ats_scoring():
    return {"message": "ATS scoring agent called"}

@router.post("/cover-letter")
async def call_cover_letter():
    return {"message": "Cover letter agent called"}

@router.post("/interview-prep")
async def call_interview_prep():
    return {"message": "Interview prep agent called"}

@router.post("/career-roadmap")
async def call_career_roadmap():
    return {"message": "Career roadmap agent called"}

@router.post("/salary-insights")
async def call_salary_insights():
    return {"message": "Salary insights agent called"}
