from datetime import datetime, timedelta

def clock():
    now = datetime.utcnow()  # Usar UTC explícitamente
    start_of_day = datetime(now.year, now.month, now.day)
    milliseconds_since_start_of_day = (now - start_of_day).total_seconds() * 1000
    new_time = milliseconds_since_start_of_day * 48
    new_date = start_of_day + timedelta(milliseconds=new_time)
    return new_date.strftime('%Y-%m-%d %H:%M:%S')