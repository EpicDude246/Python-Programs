num = input("Number ")


try:
    num = int(num)

except ValueError:
    print("This is not a number...")
    quit()


v = 1


for a in range(num):
    v += 1
    if v == num:
        print("The num is prime.")
        quit()
    if num % v == 0:
        print("The number is not prime.")
        quit()


print("The num is neither prime nor composite")