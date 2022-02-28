import random
num = random.randint(1, 20)
n=0
while n != 6:
    n += 1
    answer = int(input("ANSWER"))
    if answer == num:
        print("Well Guessed!!!")
        quit()
    if answer - 7 < num < answer or answer + 7 > num > answer:
        print("Num Close!")
    else:
        print("Num Far!!!")
print("The num was", num)
    