from datetime import date, timedelta

INTERVALS = [1,3,7,14,30,60,90,120,150,180]

def build_schedule(learned_on, span_months):
    try:
        if span_months == 0 or span_months > 6:
            raise ValueError
    except ValueError:
        print("Invalid time span.")

    days = span_months * 30
    current_interval = []
    date_list = []
    for interval in INTERVALS:
        sum += interval
        if sum > days:
            break
        else:
            current_interval.add(interval)

    for interval in current_interval:
        date = learned_on + timedelta(days=interval)
        date_list.add(date)

    
