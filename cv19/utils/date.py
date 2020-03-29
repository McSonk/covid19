from datetime import datetime, timedelta

DATETIME_FORMAT = '%Y-%m-%d'

def elapsed_time(orig_date : str) -> int:
    now = datetime.now()
    delta = now - orig_date
    return delta.days


def add_days(orig_date: str, days: int):
    target = datetime.strptime(orig_date, DATETIME_FORMAT) + timedelta(days=days)
    return target.strftime(DATETIME_FORMAT)