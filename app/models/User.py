from typing import Optional

from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str
    role: int
    room: str
    fullname: str
    position: str
    date_of_birth: Optional[str] = None
    url_avatar: Optional[str] = None
    token: Optional[str] = None

class InfoUser(BaseModel):
    email: str
    room: str
    fullname: str
    position: str
    date_of_birth: Optional[str] = None
    url_avatar: Optional[str] = None

class NewUser(BaseModel):
    email: str
    password: str
    role: int
    room: str
    fullname: str
    position: str

class AccessToken(BaseModel):
    email: str
    token: str