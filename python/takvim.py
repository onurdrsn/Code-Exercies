#!/usr/bin/env python
"""
import calendar
year=2021
month=6
day=13
print(calendar.day(year, month, day))
"""
#new example

"""
import calendar
year= 2021
month=7
day=13
print(calendar.month(year,month,day))
"""

#new example

"""
import calendar
print("The calendar of year 2021 is: ")
print(calendar.calendar(2021))
"""

#new example

"""
import calendar
obj = calendar.Calendar(firstweekday = 1)
for day in obj.iterweekdays():
    print(day)
"""
#new example

import calendar

calen = calendar.Calendar()
for day in calen.itermonthdates(2021, 6):
    print(day)
