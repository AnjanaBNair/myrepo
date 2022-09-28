#!/usr/bin/python
# scheduler.py - Randomly schedule a list of people for tasks within a given range of dates 
# during week days and inputting details in a csv file.

import random
import csv
from datetime import date, timedelta

# Names of people to be scheduled.
name = ['Ade', 'Sola', 'Sule', 'Bayo', 'Sade', 'Korede', 'Anthonia']

# Date range
start_date = date(2019, 1, 1)
end_date = date(2019, 7, 14)

delta = timedelta(days=1)   # For increasing the date by 1.

random.shuffle(name)  # Initial shuffle.
no_of_members = len(name)

dictwrite = {}  # For writing names of members into the csv file. 
dictweek = {}   # For writing dates into the csv file.

i = 0

month = start_date.strftime('%B')

content_table = open('content_table.csv', 'w', newline='')
content_writer = csv.DictWriter(content_table, ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
content_writer.writeheader()
content_writer.writerow({'Monday': month})

while start_date <= end_date:
    day = start_date.strftime('%A')
    date = start_date.strftime('%d-%m-%y')

    # Skip Saturdays and Sundays.
    if day == 'Saturday' or day == 'Sunday':
        start_date += delta
        continue

    # Add data to respective dictionaries with days of the week as the keys.
    dictweek[day] = date
    dictwrite[day] = name[i]
    
    # Enter rows of csv file every Friday and leaving a row empty.
    if day == 'Friday':
        content_writer.writerow(dictweek)
        content_writer.writerow(dictwrite)
        content_writer.writerow({})

        # Check if it is a new month.
        new_month = start_date.strftime('%B')

        if new_month != month:
            content_writer.writerow({'Monday': new_month})
            month = new_month
        
        # Emptying the dictionaries after writing the rows.
        dictwrite = {}
        dictweek = {}
    
    # Increasing the date.
    start_date += delta
    i += 1

    # When all members have been given a date, reshuffle the list and start again.
    if i > (no_of_members - 1):
        i = 0  # Start from beginning.
        random.shuffle(name)  # Reshuffling list after all members had worked.

# When we get to the last week in the range, and it does not end on a Friday,
# we input the name and dates still in the dictionaries to the csv file.
if dictwrite != {}:
    content_writer.writerow(dictweek)
    content_writer.writerow(dictwrite)

content_table.close()
