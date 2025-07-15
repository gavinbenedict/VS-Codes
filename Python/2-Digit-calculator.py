a,b=0,0
def accept():
    global a,b
    a=int(input("Enter for A:"))
    b=int(input("Enter for B:"))
def choose():
    print("Choose:\n\nA-Addition\nS-Subtraction\nM-Multiplication\nD-Division")
    s=input() 
    match s:
        case "a":
            print(add(a,b))
        case "s":
            print(sub(a,b))
        case "m":
            print(mul(a,b))
        case "d":
            print(div(a,b))
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
accept()
choose()