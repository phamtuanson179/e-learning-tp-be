import starlette.status

from app.repositories.UserRepo import UserRepo
from app.models.User import InfoUser, NewUser, User
from app.exceptions.CredentialException import CredentialException
from app.utils.AuthUtil import AuthUtil

class UserService:
    
    def __init__(self):
        self.__name__= "UserService"
        self.repo = UserRepo()


    def create_user(self, new_user: NewUser):
        _u = self.repo.get_user_by_email(new_user.email)
        if _u:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "User already exists")
        
        hash_password = AuthUtil.hash_password(new_user.password)
        user = User(email=new_user.email, password= hash_password, role=new_user.role, room=new_user.room, fullname=new_user.fullname, position=new_user.position, date_of_birth="", url_avatar="", token="")
        res = self.repo.create_user(user)
        return "Register success"

    def get_user(self, email: str):
        _u = self.repo.get_info_user(email)
        if not _u:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "User not exists")
        return _u

    def update_user(self, info: InfoUser):
        res = self.repo.update_user(info)
        if not res:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Error")
        return "Update success"