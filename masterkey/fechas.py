from datetime import datetime, timedelta

def fechas():
    day = datetime.now()
    dt = datetime.strptime(day, '%d/%b/%Y')
    start = dt - timedelta(days=dt.weekday())
    end = start + timedelta(days=6)
