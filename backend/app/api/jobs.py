from fastapi import APIRouter

router = APIRouter()

@router.get("/search")
async def search_jobs():
    return {"jobs": []}

@router.get("/saved")
async def saved_jobs():
    return {"saved_jobs": []}

@router.post("/match")
async def match_jobs():
    return {"matches": []}

@router.get("/{job_id}")
async def get_job(job_id: int):
    return {"job_id": job_id}
