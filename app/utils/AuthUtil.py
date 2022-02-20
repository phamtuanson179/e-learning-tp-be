import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.security import HTTPBearer

from app.configs.Config import auth_config

class AuthUtil:

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    reusable_oauth2 = HTTPBearer(scheme_name='Authorization')

    def verify_password(plain_password, hashed_password):
        return AuthUtil.pwd_context.verify(plain_password, hashed_password)

    def hash_password(password):
        return AuthUtil.pwd_context.hash(password)

    def create_access_token(email: str) -> str:
        expires_delta = timedelta(minutes=auth_config['expire_minutes'])
        expires_at = datetime.utcnow() + expires_delta
        to_encode = {
            "email": email, 
            "exp": expires_at
            }
        encoded_jwt = jwt.encode(to_encode, key=auth_config['secret_key'], algorithm=auth_config['algorithm'])
        return encoded_jwt

