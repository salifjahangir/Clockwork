from datetime import timedelta

INTERVALS = [1,3,7,14,30,60,90,120,150,180]

def build_schedule(learned_on, span_months):
    """Takes a date object and number of months and returns a list of interval, date tuples"""
    if span_months <= 0 or span_months > 6:
            raise ValueError("Invalid month span.")

    days = span_months * 30
    due_list = []
    for interval in INTERVALS:
        if interval > days:
            continue
        else:
            due_date = learned_on + timedelta(days=interval)
            due_list.append((interval, due_date))

    return due_list
