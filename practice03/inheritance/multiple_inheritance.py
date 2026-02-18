"""
What is Multiple Inheritance?

Multiple inheritance is when a class inherits from more than one parent class.

So instead of:

Child → Parent


We have:

Child → Parent1 + Parent2

Basic Syntax:

class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass
"""
#example:
class Father:
    def skills(self):
        print("Plumbing")

class Mother:
    def talent(self):
        print("Singing")

class Child(Father, Mother):
    pass

c = Child()

c.skills()
c.talent()