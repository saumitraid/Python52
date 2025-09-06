# Parent class
class Animal:
    def eat(self):
        print("Eating......")

# Child class
class Dog(Animal):
    def bark(self):
        print("Barking......")

# Child class
class Pupies(Dog):
    def weap(self):
        print("Weaping......")
    
    def eat(self):
        print("Drinking milk......")

ob=Pupies()
ob.weap()
ob.bark()
ob.eat()

