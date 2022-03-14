import starlette.status
import jwt
from app.configs.Config import auth_config
from app.repositories.UserRepo import UserRepo
from app.repositories.ExamRepo import ExamRepo
from app.models.User import NewUser, User
from app.models.Exam import Exam
from app.exceptions.CredentialException import CredentialException
from app.utils.AuthUtil import AuthUtil

class UserService:
    
    def __init__(self):
        self.__name__= "UserService"
        self.repo = UserRepo()
    
    def create_user(self, new_user: NewUser, token: str):
        payload = jwt.decode(token, auth_config['secret_key'], algorithms=auth_config['algorithm'])
        email: str = payload.get("email")
        user_call_api = self.repo.get_user_by_email(email)

        if not user_call_api:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Error user call api not exist")

        hash_password = AuthUtil.hash_password(new_user.password)
        user = User(email=new_user.email, password= hash_password, role=new_user.role, room=new_user.room, fullname=new_user.fullname, position=new_user.position, date_of_birth="", url_avatar="", token="")
        if(new_user.role == 1 or new_user.role == 0):
            if(user_call_api.role == 1 or user_call_api.role == 2):
                _u = self.repo.get_user_by_email(new_user.email)
                if _u:
                    raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "User already exists")
                res = self.repo.create_user(user)
                return "Create success"
            else:
                raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")
        elif(new_user.role == 2):
            if(user_call_api.role == 2):
                _u = self.repo.get_user_by_email(new_user.email)
                if _u:
                    raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "User already exists")
                res = self.repo.create_user(user)
                return "Create success"
            else:
                raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Permission denied")

    def delete_user(self, email: str):
        res = self.repo.delete_user(email)
        return "Delete success"

    def get_all_admin(self):
        list_admins = self.repo.get_all_admin()
        return list_admins

    def get_user(self, email: str):
        _u = self.repo.get_info_user(email)
        if not _u:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "User not exists")
        return _u

    def get_users_in_room(self, room: str):
        list_users = self.repo.get_users_in_room(room)
        return list_users

    def update_admin(self, info: User):
        res = self.repo.update_admin(info)
        if not res:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Error")
        return "Update success"

    def update_user(self, info: User):
        res = self.repo.update_user(info)
        if not res:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Error")
        return "Update success"