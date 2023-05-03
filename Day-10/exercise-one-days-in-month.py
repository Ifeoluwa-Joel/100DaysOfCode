"""
Note to future self:
The code for the function is_leap was brought from Coding Exercise 3.3
in case you want to revisit that. However, the outputs were not Boolean
but rather "Leap Year" and "Not Leap Year".
It was changed to Boolean in today's exercise which reason you will see in
the context of this program.
"""

def is_leap(year):
    """Returns a Boolean. True if a year is a leap year and False if otherwise"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    """Receives a year and a month then returns the number of
    days in that particular month. It also takes leap years into account"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return "Invalid month! Maybe that's a Kepler 452b month."

    is_year_leap = is_leap(year)
    if is_year_leap:
        if month == 2:
            return 29
        else:
            return month_days[month - 1]
    elif not is_year_leap:
        return month_days[month - 1]

# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


'''
Ouch, my days_in_month function works but it is slightly more complicated to read.
Angela's code embarrassed mine 🤣🤣🤣

Here is Angela's code:
'''

""""
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]

clean and nice, I love it! 😘
"""