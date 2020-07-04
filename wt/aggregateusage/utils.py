import datetime

def getDateFormatted(dt):
    dtt = datetime.datetime.strptime(dt, '%d.%m.%Y')
    date = dtt.strftime("%Y-%m-%d")
    return date
