# OVERRIDING - a child can replace parent method
# example:
class Animal:
    def __init__(self, name):
        self.name = name

    def noise(self):
        print("Animal makes a sound")

class Dog(Animal):
    def noise(self):   # overriding
        print("Woof!")
#creating an object
d =Dog("Buddy")

print(d.name)
d.noise()