from fastapi import APIRouter, Header

from app.services.UserService import UserService
from app.services.AuthService import AuthService
from app.services.ExamService import ExamService
from app.models.User import NewUser, User
from app.models.Exam import NewExam

router = APIRouter()

@router.post("/admin/add_exam")
async def create_exam(new_exam: NewExam, token: str = Header(None)):
    if AuthService().validate_token(token):
        if UserService().check_admin_permission(token):
            res = ExamService().create_exam(new_exam, token)
            return res

@router.post("/admin/add_user")
async def create_user(new_user: NewUser, token: str = Header(None)):
    if AuthService().validate_token(token):
        if (new_user.role == 2):
            if not UserService().check_super_admin_permission(token):
                return "Permission denied"
        elif not UserService().check_admin_permission(token):
            return "Permission denied"
        res = UserService().create_user(new_user)
        return res

@router.delete("/admin/delete_exam")
async def delete_exam(id: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        if UserService().check_admin_permission(token):
            res = ExamService().delete_exam(id)
            return res

@router.delete("/admin/delete_user")
async def delete_user(email: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        if UserService().check_admin_permission(token):
            res = UserService().delete_user(email)
            return res

@router.post("/admin/get_all_admin")
async def get_all_admin(token: str = Header(None)):
    if AuthService().validate_token(token):
        if UserService().check_super_admin_permission(token):
            res = UserService().get_all_admin()
            return res

@router.post("/admin/get_all_super_admin")
async def get_all_super_admin(token: str = Header(None)):
    if AuthService().validate_token(token):
        if UserService().check_super_admin_permission(token):
            res = UserService().get_all_super_admin()
            return res

@router.post("/admin/get_users_in_room")
async def get_users_in_room(room: str, token: str = Header(None)):
    if AuthService().validate_token(token):
        if UserService().check_admin_permission(token):
            res = UserService().get_users_in_room(room)
            return res

@router.put("/admin/update_admin")
async def update_admin(info: User, token: str = Header(None)):
    if AuthService().validate_token(token):
        if (info.role == 2):
            if not UserService().check_super_admin_permission(token):
                return "Permission denied"
        elif (info.role == 1):
            if not UserService().check_admin_permission(token):
                return "Permission denied"
        res = UserService().update_admin(info)
        return res