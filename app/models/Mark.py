from typing import Optional

from pydantic import BaseModel

class Mark(BaseModel):
    id: Optional[str] = None
    user_id: str
    exam_id: str
    point: int
    max_point: int
    is_pass: bool
    duration: int
