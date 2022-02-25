import starlette.status

from app.repositories.ExamRepo import ExamRepo
from app.models.Exam import Exam
from app.exceptions.CredentialException import CredentialException

class ExamService:
    
    def __init__(self):
        self.__name__= "ExamService"
        self.repo = ExamRepo()

    def create_exam(self, new_exam: Exam):
        res =  ExamRepo().create_exam(new_exam)
        return "Create exam success"

    def delete_exam(self, id: str):
        if self.get_exam(id):
            res = ExamRepo().delete_exam(id)
            return "Delete success"

    def get_exam(self, id: str):
        _u = ExamRepo().get_exam(id)
        if not _u:
            raise CredentialException(status_code=starlette.status.HTTP_412_PRECONDITION_FAILED, message= "Exam not exists")
        return _u

    def get_exams_for_room(self, room: str):
        list_exams = self.repo.get_exams_for_room(room)
        return list_exams