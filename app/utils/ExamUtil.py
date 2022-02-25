from app.models.Exam import Exam

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

    def nested_dict(self, obj: Exam):
        if not  hasattr(obj,"__dict__"):
            return obj
        result = {}
        for key, val in obj.__dict__.items():
            element = []
            if isinstance(val, list):
                for item in val:
                    element.append(self.nested_dict(item))
            else:
                element = self.nested_dict(val)
            result[key] = element
        return result