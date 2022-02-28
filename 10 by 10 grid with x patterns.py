#Border

for x in range(10):
    for y in range(10):
        if x==0 or x==9 or y==0 or y==9:
            print("x", end=" ")
        else:
            print("o", end=" ")
    print("")



#Diagonal
 
for x in range(10):
    for y in range(10):
        if y+x==9:
            print("x", end=" ")
        else:
            print("o", end=" ")
    print("")




#Reverse Diagonal 

for x in range(10):
    for y in range(10):
        if y==x:
            print("x", end=" ")
        else:
            print("o", end=" ")
    print("")






