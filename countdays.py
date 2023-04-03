from datetime import date
from dateutil.parser import parse


def count_days(start_date_str, end_date_str):
    # validate input
    try:
        start_date = parse(start_date_str).date()
        end_date = parse(end_date_str).date()
    except ValueError:
        return None

    # calculate number of days
    delta = end_date - start_date
    days = delta.days

    return days
