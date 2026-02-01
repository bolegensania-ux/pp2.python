# The For loop
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

"""
Example:                                            Result:
Print each fruit in a fruit list:                    apple
                                                     banana
fruits = ["apple", "banana", "cherry"]               cherry
for x in fruits:
  print(x)

"""

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters
"""
Example:
Loop through the letters in the word "banana":

for x in "banana":
  print(x)
"""

# the break statement
# With the break statement we can stop the loop before it has looped through all the items

"""
Example:
Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
"""

#the  CONTINUE statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next

"""
Example:
Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
"""

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

"""
Example: 
Using the range() function:                Result:
                                           0          3
for x in range(6):                         1          4
  print(x)                                 2          5
"""        
# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
"""
Example
Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)
"""        
"""
result is:
2
5
8
11
14
17
20
23
26
29
"""        
"""
Nested Loops
A nested loop is a loop inside a loop.

The "inner loop" will be executed one time for each iteration of the "outer loop"

Example:
Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

result is:
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
"""               