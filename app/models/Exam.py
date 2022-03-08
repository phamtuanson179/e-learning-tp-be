from typing import Optional, List
from pydantic import BaseModel

from app.models.Question import Question

class Exam(BaseModel):
    id: Optional[str] = None
    name: str
    min_point_to_pass: int
    duration: int
    created_by: str
    require_rooms: List[str]
    questions: List[Question]

class Result(BaseModel):
    id: Optional[str] = None
    user_id: str
    exam_id: str
    point: int
    max_point: int
    is_pass: bool
    duration: int