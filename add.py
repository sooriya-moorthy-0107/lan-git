def add(a,b):
    print(f" the sum of {a} and {b} is {a+b}")

def addmore():
    i=int(input("enter the number of values you want to add: "))
    s=0
    for n in range(i+2):
        num=int(input("enter the number: "))
        s+=1
    print(f" the sum of the entered numbers is {s}")

add(80000,75693)
addmore()

