from datetime import datetime


def time_check():
    time = datetime.now().strftime('%H:%M')
    day = datetime.now().strftime('%D')
    return time, day
