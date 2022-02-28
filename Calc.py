


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

x=input("Number1| ")
if x=="pi" or x=="Pi":
    x=math.pi
y=input("Operation, +,-,*,/,^, Factorial, SquareRoot | ")

if y=="Factorial" or y=="SquareRoot":
    e=Calc2(int(x),y) 
    print(x,y,"=",e)
else:
    z=input("Number2| ")
    if z=="pi" or z=="Pi":
        z=math.pi
    e=Calc(int(x),y,int(z))
    print(x,y,z,"=",e)
    
v=""


for x in range(100):
    y=input("Operation| ")
    z=input("Number| ")
    if z=="pi" or z=="Pi":
        z=math.pi
    v=e
    e=Calc(int(e),y,int(z))
    print(v,y,z,"=",e)






