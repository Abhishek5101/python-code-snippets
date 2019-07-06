import datetime
import pytz

# fmt = '%m-%d %H:%M %Z%z'
# starter = datetime.datetime(2015, 10, 21, 4, 29)
# us_pacific = pytz.timezone('US/Pacific')
# local = us_pacific.localize(starter)
# pytz_string = local.strftime(fmt)

"""
Intercontinental meeting scheduler
Convert given D&T by the user and convert it to 6 different TZs
1. Convert the given datetime into UTC and then 
2. Convert that into 6 timezones
"""

OTHER_TIMEZONES = [
    pytz.timezone('US/Pacific'),
    pytz.timezone('Pacific/Auckland'),
    pytz.timezone('Asia/Calcutta'),
    pytz.timezone('UTC'),
    pytz.timezone('Europe/Paris'),
    pytz.timezone('Africa/Khartoum')
]

fmt = '%Y-%m-%d %H:%M:%S %Z%z'

while True:
    date_input = input("When is your meeting. Use MM/DD/YYYY HH:MM\n")
    try:
        local_date = datetime.datetime.strptime(date_input, '%m/%d/%Y %H:%M')
    except ValueError:
        print(f"{date_input} doesn't work")
    else:
        local_date = pytz.timezone('Asia/Calcutta').localize(local_date)
        utc_date = local_date.astimezone(pytz.utc)

        output = []
        for timezone in OTHER_TIMEZONES:
            output.append(utc_date.astimezone(timezone))
        for appointment in output:
            print(appointment.strftime(fmt))
        break
