# Evaluate Values and Variables
# The bool() function allows you to evaluate any value, and give you True or False in return

"""
Example
Evaluate a string and a number:

print(bool("Hello"))   #(True)
print(bool(15))        #(True)
"""

"""
Example
Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))
"""

"""
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""

"""
Example:

The following will return True:

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
"""

"""
Some Values are False

In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

Example:
The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
""" 

"""
Functions can Return a Boolean

You can create functions that returns a Boolean Value:

Example:

def myFunction() :
  return True

print(myFunction())
"""