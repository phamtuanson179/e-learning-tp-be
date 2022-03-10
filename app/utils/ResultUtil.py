from app.models.Result import Result

class ResultUtil:

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