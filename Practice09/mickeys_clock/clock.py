import datetime

def get_angles():

    now = datetime.datetime.now()
    sec = now.second
    min = now.minute

    sec_angle = sec * 6
    min_angle = min * 6

    return sec_angle, min_angle