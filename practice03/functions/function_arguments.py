# PARAMERTER AND ARGUMENT
# PARAMETER - is a variable listed in the function defifnition, it acts like a placeholder for the value that the function will receive

"""
example:

def greet(name):    # <-- name is a parameter
    print("hello", name)
"""

# ARGUMENT - is the actual value you pass to the function when you call it

"""
example:

def greet(name):
    print("hello", name)

greet("Saniya")  # call the function and pas an argument to it
"""

# number of arguments:
# by default, function must be called with the correct number of arguments
"""
Example:
This function expects 2 arguments, and gets 2 arguments::

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
"""

# DEFAULT PARAMETER VALUES
# we can assign default parameter values, if the function is called without an argument, it uses the default value:

"""
Example:
def my_function(name = "friend"):  # default parameter
  print("Hello", name)

my_function()
"""

# KEYWORD ARGUMENTS
# we can send arguments as: "key = value" syntax

"""
Example:

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")   # keyword argument
"""

# POSITIONAL ARGUMENTS
# When you call a function with arguments without using keywords, they are called positional arguments.
# Positional arguments must be in the correct order. 

# PASSING DIFFERENT DATA TYPES AS ARGUMENTS
# we can assign different kind of data types as arguments:

"""
example:

def my_function(friuts):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)
"""

"""
Example:
Sending a dictionary as an argument:

def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)
"""

# POSITIONAL ONLY ARGUMeNTS
# to specif yhtat the function has the only positional argument, add , / after the paramenter in the function definition
"""
def my_function(name, /):
  print("Hello", name)

my_function("Emil")
"""
# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:
"""
Example:

def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")
"""