#The Elif Keyword
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

"""
Example:

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
"""
#In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".

# You can have as many elif statements as you need. Python will check each condition in order and execute the first one that is true
"""
Example
Testing multiple conditions:

score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")      # result is "C"
"""
