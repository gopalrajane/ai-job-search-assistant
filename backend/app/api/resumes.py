from fastapi import APIRouter

router = APIRouter()

@router.post("/upload")
async def upload_resume():
    return {"message": "Resume uploaded"}

@router.get("/")
async def list_resumes():
    return {"resumes": []}

@router.get("/{resume_id}")
async def get_resume(resume_id: int):
    return {"resume_id": resume_id}

@router.delete("/{resume_id}")
async def delete_resume(resume_id: int):
    return {"deleted_resume_id": resume_id}
