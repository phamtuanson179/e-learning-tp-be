import jwt
from datetime import datetime

from app.repositories.UserRepo import UserRepo
from app.exceptions.CredentialException import CredentialException
from app.utils.AuthUtil import AuthUtil
from app.configs.Config import auth_config

class AuthService:
    
    def __init__(self):
        self.__name__= "AuthService"
        self.repo = UserRepo()

    async def authenticate_user(self, email: str, password: str):
        try:
            user = self.repo.get_user_by_email(email)
            if not AuthUtil.verify_password(password, user.password):
                raise CredentialException(message="UNAUTHORIZED")
        except Exception as e:
            print(e)
            raise CredentialException(message="UNAUTHORIZED")

        access_token = AuthUtil.create_access_token(email)
        res = self.repo.update_token(email, access_token)
        return {"access_token": access_token, "token_type": "bearer"}

    def validate_token(self, token: str):
        try:
            payload = jwt.decode(token, auth_config['secret_key'], algorithms=auth_config['algorithm'])
            email: str = payload.get("email")
            exp = payload.get("exp")
            expire = datetime.fromtimestamp(exp)
            if not self.repo.get_token_by_email(email):
                raise CredentialException(message="Could not validate credentials")
            if token != self.repo.get_token_by_email(email).token:
                raise CredentialException(message="Could not validate credentials")
            if expire < datetime.utcnow():
                raise CredentialException(message="Token expired")
        except:
            raise CredentialException(message="Could not validate credentials")
        return True
