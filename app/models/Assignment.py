from typing import Optional

from pydantic import BaseModel

class Assignment(BaseModel):
    email: str
    
    role: Optional[int] = None
    room: str
    fullname: str
    position: str
    date_of_birth: Optional[str] = None
    url_avatar: Optional[str] = None
    token: Optional[str] = None
