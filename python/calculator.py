def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice=int(input("Enter your choice:-"))
if choice>=1 and choice<=4:
    n1=int(input("Enter 1st Number:-"))
    n2=int(input("Enter 2nd Number:-"))
    match choice:
        case 1:
            print("Addition is",add(n1,n2))
        case 2:
             print("Subtraction is",sub(n1,n2))
        case _:
            print("Wrong input")
else:
    print("Wrong choice")