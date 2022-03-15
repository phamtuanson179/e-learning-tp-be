import starlette.status
import jwt
from app.repositories.ExamRepo import ExamRepo
from app.repositories.ResultRepo import ResultRepo
from app.models.Exam import Exam, NewExam
from app.models.Result import Result
from app.exceptions.CredentialException import CredentialException
from app.configs.Config import auth_config

class ExamService:
    
    def __init__(self):
        self.__name__= "ExamService"
        self.repo = ExamRepo()

    def create_exam(self, new_exam: NewExam, token):
        payload = jwt.decode(token, auth_config['secret_key'], algorithms=auth_config['algorithm'])
        email: str = payload.get("email")
        exam = Exam(name=new_exam.name, 
                    min_point_to_pass=new_exam.min_point_to_pass, 
                    duration=new_exam.duration,
                    require_rooms=new_exam.require_rooms,
                    image=new_exam.image,
                    questions=new_exam.questions,
                    created_by=email)
        res =  ExamRepo().create_exam(exam)
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

    def get_exam_history(self, user_id: str, exam_id: str):
        list_history = ResultRepo().get_exam_history(user_id, exam_id)
        return list_history

    def get_exam_ranking(self, exam_id: str):
        list_history = ResultRepo().get_exam_ranking(exam_id)
        return list_history

    def save_result(self, new_result: Result):
        res =  ResultRepo().save_result(new_result)
        return "Save result success"