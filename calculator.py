print('''
 _____________________
|  _________________  |
| |            0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

''')

def add(a,b):
    sum = a+b
    return sum
def sub(a,b):
    sub=a-b
    return sub
def mul(a,b):
    mul=a*b
    return mul
def div(a,b):
    div=a/b
    return div

def new():
    flag=0
    x=float(input("Enter the first number: "))
    print("+,-,*,/")
    op=input("Pick an operator: ")
    y=float(input("Enter the next number: "))
    if op=="+":
        result=add(x,y)
    elif op=="-":
        result=sub(x,y)
    elif op=="*":
        result=mul(x,y)
    elif op=="/":
        result=div(x,y)
    else:
        print("You picked up the wrong operator!")
        flag=1
    if flag==0:
        print(f"{x} {op} {y} = {result}")
        return result


def conti(answer):
    flag=0
    x=answer
    print("+,-,*,/")
    op=input("Pick an operator: ")
    y=float(input("Enter the next number: "))
    if op=="+":
        result=add(x,y)
    elif op=="-":
        result=sub(x,y)
    elif op=="*":
        result=mul(x,y)
    elif op=="/":
        result=div(x,y)
    else:
        print("You picked up the wrong operator!")
        flag=1
    if flag==0:
        print(f"{x} {op} {y} = {result}")
        return result

# 
result=new()
choice="y"
while choice=="y" or choice=="n":
    choice=input(f"type 'y' to continue with {result}, or type 'n' to start a new a calculation")
    if choice=="y":
        result=conti(result)
    elif choice=="n":
        result=new()



