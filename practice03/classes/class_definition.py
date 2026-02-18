# What is a class in python?

# class in python is like a blueprint for creating objects

# blueprint defines atributes(data/variables), methods(functions)

"""
real life example:
imagine a car blueprint:
the blueprint defines:
1) color
2) brand
3) speed
"""

"""
basic syntax:
class ClassName:
    pass
    
class -> is a keyword
ClassName -> usually starts with a capital letter
pass -> means "do nothing" acts like a placeholder
"""

# adding data:
"""
class Student:
    def __init__(self, name, age)    #__init__ - use it to add data   # self - the object we have created
    self.name = name
    self.age = age


self.name = name
Left side → variable inside the object
Right side → value we pass when creating it

# creating a project:
s1 = Student("Saniya", 18)

Here's what happens internally:

Python creates a new object → s1

It calls __init__

"Saniya" goes into name

18 goes into age

They get stored inside s1

print(s1.name)                  output: Saniya
print(s1.age)                   output: 18
"""