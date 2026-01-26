# there are three numeric types in python:
"""
1) int
2) float
3) complex
"""

"""
Variables of numeric types are created when you assign a value to them:

x = 1    # int
y = 2.8  # float
z = 1j   # complex
"""
#int is a whole number which can be postive or negative, without decimals
# float is a floating point number, which has one or more decimals
#Float can also be scientific numbers with an "e" to indicate the power of 10.
#Complex numbers are written with a "j" as the imaginary part

"""
Type Conversion
You can convert from one type to another with the int(), float(), and complex() methods:

Example:
Convert from one type to another:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
"""

#if we wantt o generate a random number, we need to import "random" library
"""
import random

print(random.randrange(1, 10))
"""