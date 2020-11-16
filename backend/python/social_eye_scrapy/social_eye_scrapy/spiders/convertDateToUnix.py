import datetime
from datetime import timedelta
import time


def convertThaiToEnglish(arg):
    switcher = {
        "ม.ค.": 1,
        "ก.พ.": 2,
        "มี.ค.": 3,
        "เม.ย.": 4,
        "พ.ค.": 5,
        "มิ.ย.": 6,
        "ก.ค.": 7,
        "ส.ค.": 8,
        "ก.ย.": 9,
        "ต.ค.": 10,
        "พ.ย.": 11,
        "ธ.ค.": 12
    }
    return switcher.get(arg, "invalid")


def convertDateToUnix(thaitime):
    if len(thaitime) == 15:
        date = now.day
        month = now.month
        year = now.year
        hour = int(thaitime[slice(7, 9)])
        minute = int(thaitime[slice(10, 12)])
        date_register = datetime.datetime(year, month, date, hour, minute)
        date_unix = int(time.mktime(date_register.timetuple()))
    elif len(thaitime) == 17:
        date = yesterday.day
        month = yesterday.month
        year = yesterday.year
        hour = int(thaitime[slice(9, 11)])
        minute = int(thaitime[slice(12, 14)])
        date_register = datetime.datetime(year, month, date, hour, minute)
        date_unix = int(time.mktime(date_register.timetuple()))
    else:
        date = int(thaitime[slice(2)])
        month = int(convertThaiToEnglish(thaitime[slice(3, 7)]))
        year = int(thaitime[slice(8, 10)]) + 1957
        hour = int(thaitime[slice(11, 13)])
        minute = int(thaitime[slice(14, 16)])
        date_register = datetime.datetime(year, month, date, hour, minute)
        date_unix = int(time.mktime(date_register.timetuple()))
    # print(date)
    # print(month)
    # print(year)
    # print(hour)
    # print(minute)
    print(date_register)
    print(date_unix)
    return date_unix


now = datetime.datetime.now()
yesterday = now - timedelta(days=1)

# convertDateToUnix("13 พ.ย. 63 19:44 น.")
# convertDateToUnix("11 พ.ย. 63 17:52 น.                    ")
# convertDateToUnix("26 ก.ย. 63 05:54 น.                    ")
# convertDateToUnix("07 พ.ย. 63 01:01 น.")
# convertDateToUnix("วันนี้ 18:16 น.")