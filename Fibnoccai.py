x=input("How many numbers of the fibonacci sequence do you want?")
a=0
b=1
c=""
for z in range(int(x)):
    c=a+b
    a=b
    b=c
    print(c)