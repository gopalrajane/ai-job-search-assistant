from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def list_users():
    return {"users": []}

@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

@router.put("/{user_id}")
async def update_user(user_id: int):
    return {"updated_user_id": user_id}
