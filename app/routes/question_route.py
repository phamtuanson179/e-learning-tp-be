from fastapi import APIRouter, Depends, Header
from app.services.auth_service import AuthService
from app.services.subject_service import SubjectService
from app.models.Subject import Subject
from app.routes.auth_route import oauth2_scheme

router = APIRouter(prefix="/question")

@router.get("/get-all")
async def get_all_subject(token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        pass

@router.get("/get-by-id")
async def get_exam_history(alias: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        pass

@router.post("/create")
async def create_subject(subject: Subject, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        pass

@router.put("/update")
async def update_subject(subject: Subject, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        pass

@router.delete("/delete")
async def delete_subject(alias: str, token: str = Depends(oauth2_scheme)):
    if AuthService().validate_token(token):
        pass
