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

