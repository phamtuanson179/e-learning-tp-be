from datetime import datetime

class TimeUtil:

    def to_str(time: datetime) -> str:
        return time.strftime("%Y-%m-%d %H:%M:%S")