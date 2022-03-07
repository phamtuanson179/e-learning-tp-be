from fastapi import APIRouter, Header

from app.services.UserService import UserService
from app.services.AuthService import AuthService
from app.models.User import User, NewUser
from app.services.ExamService import ExamService
from app.models.User import User

router = APIRouter()

@router.get("/get_exam")
async def get_exam(id: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = ExamService().get_exam(id)
        return res

@router.get("/get_exams_for_room")
async def get_exams_for_room(room: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = ExamService().get_exams_for_room(room)
        return res

@router.get("/get_user")
async def get_user(email: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = UserService().get_user(email)
        return res

@router.post("/mark_exam")
async def mark_exam(room: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = ExamService().get_exams_for_room(room)
        return res

@router.put("/update_user")
async def update_user(info: User, token: str = Header(None)):
    if AuthService().validate_token(token):
        res = UserService().update_user(info)
        return res