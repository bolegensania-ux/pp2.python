# Write a Python program to drop microseconds from datetime.

import datetime
now = datetime.datetime.now()
no_microseconds = now.replace(microsecond=0)
print("original;", now)
print("without microseconds:", no_microseconds)