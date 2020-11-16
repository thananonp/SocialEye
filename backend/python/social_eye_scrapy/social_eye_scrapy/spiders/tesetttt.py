import datetime
import time


def convertThaiToEnglist(arg):
    switcher = {
        "ม.ค.": 1,
        "ก.พ.": 2,
        "ม.ค.": 3,
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


"วันนี้ 13:39 น."
"เมื่อวาน 15:56 น."
thaitime = "13 พ.ย. 63 19:44 น."
now = datetime.datetime.now()
if(len(thaitime) == 15):
    slicehour = slice(5, 7)
    sliceminute = slice(8, 10)
elif (len(thaitime) == 17):
    pass

else:
    slicedate = slice(2)
    slicemonth = slice(3, 7)
    sliceyear = slice(8, 10)
    slicehour = slice(11, 13)
    sliceminute = slice(14, 16)
    date = int(thaitime[slice(2)])
    month = int(convertThaiToEnglist(thaitime[slice(3, 7)]))
    year = int(thaitime[slice(8, 10)]) + 1957
    hour = int(thaitime[slice(11, 13)])
    minute = int(thaitime[slice(14, 16)])
    dateRegister = datetime.datetime(year, month, date, hour, minute)
    dateUnix = time.mktime(dateRegister.timetuple())
    # thaitimeenglish = thaitime.replace("พ.ย.", "11")
    # unixtime = time.mktime(x.timetuple())
print(date)
print(month)
print(year)
print(hour)
print(minute)
# print(convertThaiToEnglist(month))
print(dateRegister)
print(dateUnix)
# print(thaitimeenglish)
# print(x)
# print(unixtime)
