from datetime import datetime
from time import strptime

time_format = "yyyy-MM-dd'T'HH:mm:ssZ"


def get_current_date():
    now = datetime.now()
    return now.isoformat()


def get_date_from_string(date_string: str):
    return datetime.fromisoformat(date_string)
