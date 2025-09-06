class Person:
    def getName(self, name):
        print("Name is "+name)

    def walk(self):
        print("A person can walk")
    
    def talk(self):
        print("A person can talk")

ob=Person()
ob.getName('Amit')
ob.talk()
ob.walk()

ob1=Person()
ob1.getName('Ratan')
ob1.talk()
ob1.walk()