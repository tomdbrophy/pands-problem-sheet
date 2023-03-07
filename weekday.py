# Outputs whether the current day is a weekday.
# Author: Tom Brophy
# Day/Date information gotten from https://www.w3schools.com/python/python_datetime.asp
# If statement help found here: https://www.askpython.com/python/list/find-string-in-list-python

import datetime

today_date = datetime.datetime.now()
current_day = today_date.strftime("%A")

all_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays = all_days[:5]
weekend = all_days[5:]

#print('The weekdays are:', weekdays)
#print('The weekend is:', weekend)

if current_day in weekdays:
    print('Yes, unfortunately today is a weekday.')
else:
    print('It is the weekend, yay!')
