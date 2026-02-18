# *args
"""
What is *args?
The *args parameter allows a function to accept any number of positional arguments.

Inside the function, args becomes a tuple containing all the passed arguments:

Example
Accessing individual arguments from *args:

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")
"""

"""
Example:

A function that calculates the sum of any number of values:

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))
"""

# **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name
"""
Example: 
Using **kwargs to accept any number of keyword arguments:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
"""
# The **kwargs parameter allows a function to accept any number of keyword arguments.

# Inside the function, kwargs becomes a dictionary containing all the keyword arguments.