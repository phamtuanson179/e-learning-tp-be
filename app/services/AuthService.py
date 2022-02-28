import jwt
from datetime import datetime

from app.repositories.UserRepo import UserRepo
from app.services.UserService import UserService
from app.exceptions.CredentialException import CredentialException
from app.utils.AuthUtil import AuthUtil
from app.configs.Config import auth_config
from app.utils import EmailUtil
import string, random


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

    def validate_password(self, password, token: str):
        try:
            payload = jwt.decode(token, auth_config['secret_key'], algorithms=auth_config['algorithm'])
            email: str = payload.get("email")
            user = self.repo.get_user_by_email(email)
            if not AuthUtil.verify_password(password, user.password):
                raise CredentialException(message="UNAUTHORIZED")
        except Exception as e:
            print(e)
            raise CredentialException(message="UNAUTHORIZED")
        return True

    def change_password(self, email: str, password: str):
        access_token = AuthUtil.create_access_token(email)
        reset_token = self.repo.update_token(email, access_token)
        hash_password = AuthUtil.hash_password(password)
        reset_password = self.repo.update_password(email, hash_password)
        return {"access_token": access_token, "hash_password": password}

    async def handle_forgot_password(self, email: str):
        # check user exist
        res = UserService().get_user(email)
        random_password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
        
        # reset token and change password then save database
        reset_password = AuthService().change_password(email, random_password)

        # send email
        subject = "QUÊN MẬT KHẨU"
        recipient = [email]
        message = f"""
                Mật khẩu mới của bạn là:
                {random_password}
                """
        await EmailUtil.send_email(subject, recipient, message)
        
        return "Reset password complete" 

    async def handle_change_password(self, curr_pass: str, new_pass: str, confirm_pass: str, token: str):
        if not AuthService().validate_password(curr_pass, token):
            raise CredentialException(message="Current password is wrong")

        # check new password and confirm password
        if new_pass != confirm_pass:
            raise CredentialException(message="New password does not match confirm password")
        
        # reset token and change password then save database
        payload = jwt.decode(token, auth_config['secret_key'], algorithms=auth_config['algorithm'])
        email: str = payload.get("email")
        change_password = AuthService().change_password(email, new_pass)

        return "Change password complete" 
