class Person:
    def __init__(self, name):
        self.name=name

    def walk(self):
        print(self.name,"can walk")
    
    def talk(self):
        print(self.name,"can talk")

ob=Person("Ratan")
ob.walk()
ob.talk()

# WAPP for count number of object created of a class. 