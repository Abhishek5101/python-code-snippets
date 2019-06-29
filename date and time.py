import datetime

date = datetime.date.today()
#print(date.isoweekday())  #Monday - 1


# Time deltas are differences between times. So it can add/sub datetime objects


bday = datetime.date(2020, 5, 14)
today = datetime.date.today()


diff = bday - today
print(diff.total_seconds())
