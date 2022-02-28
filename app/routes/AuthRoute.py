from fastapi import APIRouter

from app.services.AuthService import AuthService
from app.models.User import Account

router = APIRouter()

@router.post("/login")
async def login(account : Account):
    res = await AuthService().authenticate_user(account.email, account.password)
    return res