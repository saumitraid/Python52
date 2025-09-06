# Parent class
class Animal:
    def eat(self):
        print("Eating......")

# Child class
class Dog(Animal):
    def bark(self):
        print("Barking......")

ob=Dog()
ob.eat()
ob.bark()