from app.models.Subject import Subject

class SubjectUtil:

    def format_subject(subject) -> Subject:
        return subject(
            name=subject["name"],
            alias=subject["alias"],
            description=subject["description"]
        )

    