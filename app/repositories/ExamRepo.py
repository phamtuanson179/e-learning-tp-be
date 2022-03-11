from app.configs.Config import prj_config
from app.utils.ExamUtil import ExamUtil
from app.utils.TimeUtil import TimeUtil
from app.utils.CommonUtil import CommonUtil
from app.models.Exam import Exam
from .__init__ import *


class ExamRepo(BaseRepo):

    def __init__(self, collection: str="exams") -> None:
        super().__init__()
        self.collection = self.mydb[collection]

    def create_exam(self, exam: Exam):
        exam.id = prj_config['alias'] + TimeUtil.get_timestamp_now()
        exam_to_dict = CommonUtil().nested_dict(exam)
        res = self.collection.insert_one(exam_to_dict)
        return res

    def delete_exam(self, id: str):
        res = self.collection.delete_one({"id" : id})
        return res

    def get_exam(self, id: str):
        exams = list(self.collection.find({"id": id}))
        count = 0
        for record in exams:
            count += 1
        if count < 1:
            return None
        else:
            return ExamUtil.format_exam(exams[0])

    def get_exams_for_room(self, room):
        exams = list(self.collection.find({"require_rooms": { "$in": [room] }}))
        list_exams = []
        for record in exams:
            list_exams.append(ExamUtil.format_exam(record))
        return list_exams
