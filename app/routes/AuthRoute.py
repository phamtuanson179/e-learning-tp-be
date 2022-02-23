from fastapi import APIRouter

from app.services.AuthService import AuthService

router = APIRouter()

@router.post("/login")
async def login(email: str, password: str):
    res = await AuthService().authenticate_user(email, password)
    return res