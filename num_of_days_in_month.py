# num_of_days_in_month.py - A Python program to get the number of days of a given month and year.

import calendar         # For monthrange function

try:
    print('Numbers of days in a particular month and year.')
    year = int(input('Please, input the year you want; e.g. 2011: '))
    month = int(input('Please input the month number; e.g. Jan - 1, Feb - 2...: '))

    print(calendar.monthrange(year, month)[1])
    # If the [1] is not included, it gives both the weekday the month started with and number of days
    # In the case of 2022, 2(Feb), it gives (1, 28), i.e. 1 - Tues, (where 0-6 ~ Mon-Sun) and 28 days

    # To take care of a case where the user input a wrong month number
except calendar.IllegalMonthError:
    print('Invalid! Please, choose between 1 - 12 for the months of the year.')
