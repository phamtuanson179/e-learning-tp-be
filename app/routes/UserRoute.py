from fastapi import APIRouter, Header

from app.services.UserService import UserService
from app.services.AuthService import AuthService
from app.models.User import InfoUser, NewUser

router = APIRouter()

@router.get("/get_user")
async def get_user(email: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = UserService().get_user(email)
        return res

@router.post("/update_user")
async def update_user(info: InfoUser, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = UserService().update_user(info)
        return res