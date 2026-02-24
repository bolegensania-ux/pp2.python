# Write a Python program to subtract five days from current date.

import datetime
current_date = datetime.datetime.now()
new_date = current_date - datetime.timedelta(days=5)
print(new_date)

# datetime.timedelta() - is used to identify difference between two dates (days= )(hours,minutes,seconds,weeks= )