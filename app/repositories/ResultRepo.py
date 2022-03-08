
from app.models.Exam import Result
from app.utils.ExamUtil import ExamUtil
from . import *


class ResultRepo(BaseRepo):

    def __init__(self, collection: str="results") -> None:
        super().__init__()
        self.collection = self.mydb[collection]

    def get_history_a_exam(self, user_id, exam_id):
        res = self.collection.find({"user_id": user_id, "exam_id": exam_id})
        list_result = []
        for result in res:
            list_result.append(ExamUtil.format_result(result))
        return list_result

    def save_result(self, testResult: Result):
        res = self.collection.insert_one(testResult.__dict__)
        return res
