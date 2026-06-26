from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
async def register():
    return {"message": "User registration"}

@router.post("/login")
async def login():
    return {"message": "User login"}

@router.post("/refresh")
async def refresh_token():
    return {"message": "Token refresh"}
