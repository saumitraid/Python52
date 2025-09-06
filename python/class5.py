class Person:
    id=0
    def __init__(self, name):
        self.name=name
        Person.id+=1

    def walk(self):
        print(self.name,"can walk")
    
    def talk(self):
        print(self.name,"can talk")

ob=Person("Ratan")
ob.walk()
ob.talk()

ob1=Person("Akas")
ob1.walk()
ob1.talk()

ob2=Person("Kamal")
ob2.walk()
ob2.talk()
print("number of object created",ob2.id)


# WAPP for count number of object created of a class. 