from fastapi import APIRouter, Header

from app.services.UserService import UserService
from app.services.AuthService import AuthService
from app.models.User import NewUser
from app.models.Exam import Exam

router = APIRouter()

@router.post("/admin/add_exam")
async def create_exam(new_exam: Exam, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = UserService().create_exam(new_exam)
        return res

@router.post("/admin/add_user")
async def create_user(new_user: NewUser, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = UserService().create_user(new_user)
        return res

@router.delete("/admin/delete_user")
async def delete_user(email: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = UserService().delete_user(email)
        return res

@router.post("/admin/get_users_in_room")
async def get_users_in_room(room: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = UserService().get_users_in_room(room)
        return res