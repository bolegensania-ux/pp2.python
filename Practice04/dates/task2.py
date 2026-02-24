# Write a Python program to print yesterday, today, tomorrow.
import datetime
#today
current = datetime.datetime.now()
#yesterday
yesterday = current - datetime.timedelta(days=1)
#tomorrow
tomorrow = current + datetime.timedelta(days=1)
print("yesterday was:",yesterday, "today is:",current, "tomorrow will be:", tomorrow)