
from app.utils.ExamUtil import ExamUtil
from app.models.Exam import Exam
from .__init__ import *


class ExamRepo(BaseRepo):

    def __init__(self, collection: str="exams") -> None:
        super().__init__()
        self.collection = self.mydb[collection]

    def create_exam(self, exam: Exam):
        res = self.collection.insert_one(exam.__dict__)
        return res

    def get_exam(self, id):
        exams = list(self.collection.find({"id": id}))
        count = 0
        for record in exams:
            count += 1
        if count < 1:
            return None
        else:
            return ExamUtil.format_exam(exams[0])