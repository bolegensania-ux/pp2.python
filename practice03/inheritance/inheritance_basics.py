# Inheritance - allows one class to inherit atributes and methods of another class

# syntax:

#class Parent:
     #pass
#class Child(Parent):
     #pass

# example:

class Animal:     #parent class
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    pass

s1 = Dog("Buddy")
print(s1.name)