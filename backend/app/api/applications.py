from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_applications():
    return {"applications": []}

@router.post("/")
async def create_application():
    return {"message": "Application created"}

@router.get("/{application_id}")
async def get_application(application_id: int):
    return {"application_id": application_id}

@router.put("/{application_id}/status")
async def update_application_status(application_id: int):
    return {"updated_application_id": application_id}
