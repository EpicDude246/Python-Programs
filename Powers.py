def f(y):
    u=2
    for x in range(y):
        print(u)
        u=u+u
p=input("How many powers of do you want?|")
p=int(p)
f(p)