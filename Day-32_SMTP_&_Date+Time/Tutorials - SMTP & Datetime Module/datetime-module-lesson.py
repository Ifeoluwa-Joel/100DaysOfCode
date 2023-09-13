import datetime as dt

"""
TAP INTO CURRENT DATETIME --> datetime.now()
(NOTE: the datetime class is in lower case. It is not a module, 'dt' alias is the module).
"""
# now = dt.datetime.now()
# time = now.time()
# year = now.year
# month = now.month
# day = now.day
# minute = time.minute
# weekday = now.weekday()


# CREATING DATE-TIME OBJECT
date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4, minute=10)
print(date_of_birth)
