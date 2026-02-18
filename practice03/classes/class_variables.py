# class variables:

# a class variable - is a varible that belongs to the class itslef and is shared by all objects

# class variable is defined inside the class, but outside the methods

"""
example:

class Student:
    class_name = "Harvard"   --> # class variable

    def __init__(self, name):
      self.name = name  --> # instance variable

s1 = Student("Saniya")
s2 = Student("Alikhan")                              OUTPUT:
s1.school_name = "MIT"                               Saniya
                                                     Alikhan
print(s1.name)                                       MIT
print(s2.name)                                       Harvard
print(s1.school_name)
print(s2.school_name)
"""