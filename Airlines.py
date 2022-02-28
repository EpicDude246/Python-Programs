print("""Hello, this is a plane that flies from Seattle to New York.
The price is $300.
Minumum passengers are 2.""")

people=int(input("How many people are flying?  "))
if people <= 1:
    print("Sorry, these are too less passengers.")
    quit()
cou=input("Do you have a coupon code? Yes or No?  ")
we=people*300
if cou=="Yes" or cou=="yes":
    coupon=input("What is it?  ")
    print("Ok.")
else:
    coupon=0
    print("Ok.")

if coupon != "A" and coupon != "B" and coupon != "C" and coupon != 0 and coupon!="a" and coupon!="10" and coupon!="10%" and coupon!="b" and coupon!="20" and coupon!="20%" and coupon!="c" and coupon!="25" and coupon!="25%":
    print("Sorry, this is not a coupon code.")
    coupon=0

if coupon=="A" or coupon=="a" or coupon=="10" or coupon=="10%":
    a=(people*300)-(we*(10/100))
    t=10
elif coupon=="B" or coupon=="b" or coupon=="20" or coupon=="20%":
    a=people*300-(we*(20/100))
    t=20
elif coupon=="C" or coupon=="c" or coupon=="25" or coupon=="25":
    a=people*300-(we*(25/100))
    t=25
elif coupon==0:
    a=people*300
    t=1

f=a+(a*(8/100))
if t==10 or t==20 or t==25:
    print("coupon ",coupon,"is ",t,"%","off. There was ",people," people. The price for every person was $300. Tax is 8%. It costed $",f)
else:
    print("There was",people,"people. The price for every person was was $300. Tax is 8%. It costed",f)