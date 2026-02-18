# What is super()?

# super() is used to call a method from the parent class.

"""
Why do we need it?

When a child class overrides a method,
the parent method does NOT run automatically.

If we still want the parent logic, we use super().
"""
# example:

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call the parent constructer
        self.breed = breed

# create object
d= Dog("Buddy", "Labrador")

print(d.name)
print(d.breed)

"""
What does this line really do?
super().__init__(name)


It means:

“Go to my parent class and run its __init__ method.”
"""