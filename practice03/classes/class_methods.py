# method - is a function inside a class
# class method - works with the class itself, not individual objects
# it is defined using the @classmethod

"""
syntax:

class MyClass:
    @classmethod
    def method_name(cls, ...):   # cls is a keyword in class method, it refers to the class itself
"""

"""
example:

class Student:
    school_name = "Harvard"

    @classmethod
    def change_school(cls, new_name):
      cls.school_name = new_name

    Student.change_school("MIT")
    print(Student.school_name)

"""