shape=input("What is the shape, Rectangle-R, Square-S, Right Triangle-T")
a=""
if shape=="Rectangle" or shape=="R" or shape=="r":
    s1=float(input("What is the lenth of the base?"))
    s2=float(input("What is the lenth of the hight?"))
    a=s1*s2
    print("The area is",a)
    quit()
    
if shape=="Square" or shape=="S" or shape=="s":
    s1=float(input("What is the lenth of 1 side?"))
    a=s1*s1
    print("The area is",a)
    quit()
    
if shape=="Right Triangle" or shape=="T" or shape=="t":
    s1=float(input("What is the lenth of the base?"))
    s2=float(input("What is the lenth of the hight?"))
    v=s1*s2
    a=v/2
    print("The area is",a)
    quit()