from app.models.Exam import Exam, Result

class ExamUtil:

    def format_exam(exam) -> Exam:
        return Exam(
            id=exam["id"],
            name=exam["name"],
            min_point_to_pass=exam["min_point_to_pass"],
            duration=exam["duration"],
            created_by=exam["created_by"],
            require_rooms=exam["require_rooms"],
            questions=exam["questions"]
        )

    def format_result(result) -> Result:
        return Result(
            id=str(result["_id"]),
            user_id=result["user_id"],
            exam_id=result["exam_id"],
            point=result["point"],
            max_point=result["max_point"],
            is_pass=result["is_pass"],
            duration=result["duration"]
        )