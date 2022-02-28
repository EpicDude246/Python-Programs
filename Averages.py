x=int(input("How many numbers?"))
i=0
a=0
v=1
if x <= 0:
    print("The num is to less")
    quit()

for p in range(x):
    v=str(v)
    u=int(input("Enter number "+ v +"."))
    v=int(v)
    a=u+a
    v=v+1

s=a/x
print("Average is",s)