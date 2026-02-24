# Write a Python program to calculate two date difference in seconds.

import datetime
date1 = datetime.datetime(2026, 2, 24, 20, 0, 0)
date2 = datetime.datetime(2026, 2, 22, 22, 30, 0)
difference = date1 - date2
seconds = difference.total_seconds()
print("difference in seconds:", seconds)

# to convert the difference into seconds: .total_scores()