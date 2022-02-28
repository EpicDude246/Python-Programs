import random
def play():
    while True:
        code = random.randint(1000, 9999)
        codel = list(str(code))
        print(codel)
        f = True
        for go in range(100):
            guess = input("Guess: ")
            codea = ""
            gone = 0
            if str(code) == guess:
                print("YAY! You did it!")
                f = False
                break
            for item in guess:
                if item in codel and gone != codel.index(item):
                    codea += "Y"
                if item in codel and gone == codel.index(item):
                    codea += "R"
                if item not in codel:
                    codea += "B"
                gone += 1
            print(codea)
        if f:
            print("You failed.")
play()
