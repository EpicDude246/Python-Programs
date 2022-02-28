


import math
def Calc2(x,y):
    if y=="Factorial":
        r=(math.factorial(x))
    if y=="SquareRoot":
        r=(math.sqrt(x))
    return r

def Calc(x,y,z):
    l=""
    if y=="-":
        l=x-z
    if y=="+":
        l=x+z
    if y=="*":
        l=x*z
    if y=="/":
        l=x/z
    if y=="^":
        l=math.pow(x,z)
    return l

def check(x):
    try:
        if x.lower() == "e":
            x = math.e
        if x.lower() == "pi":
            x = math.pi
        return x
    except:
        pass

num1 = int(input("Number1| "))
num1final = check(num1)

oper=input("Operation, +,-,*,/,^, Factorial, SquareRoot | ")

try:
    if num1.lower() =="factorial" or num1.lower() =="squareRoot":
        finalnum=Calc2(num1,oper) 
        print(num1,oper,"=",finalnum)
except:
    pass
else:
    num2=int(input("Number2| "))
    num2final = check(num2)

    finalnum=Calc(num1,oper,num2)
    print(num1,oper,num2,"=",finalnum)
    
oldfinalnum = 0

while True:
    oper=int(input("Operation| "))
    num=int(input("Number| "))
    oldfinalnum = finalnum
    finalnum = check(num)

    e=Calc(oldfinalnum,oper,num)
    print(oldfinalnum,oper,num,"=",finalnum)






