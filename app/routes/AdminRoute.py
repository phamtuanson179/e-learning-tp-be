from fastapi import APIRouter, Header

from app.services.UserService import UserService
from app.services.AuthService import AuthService
from app.models.User import NewUser

router = APIRouter()

@router.post("/add_user")
async def create_user(new_user: NewUser, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = UserService().create_user(new_user)
        return res