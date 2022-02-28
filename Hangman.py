import random
import time
words = ["envy", "abacus", "yeet", "sickness", "epic", "great", "awesome", "bye"]
done = []
random.shuffle(words)
word = words[0]
num = 0
deathpoints = 0
realdeathpoints = 0
userinputword = []
for x in range(len(word)):
    userinputword.append("_")
while True:
    print(userinputword)
    input1 = input("What is the letter/word? ")
    if input1 in done:
        print("You already did this!")
        continue
    else:
        done.append(input1)
        print(f"You have done {done} already.")
    for y in range(len(word)):
        if input1.lower() == word[y]:
            userinputword[y] = input1
        else:
            deathpoints += 1
        if input1.lower() == word:
            print("Great Job!")
            time.sleep(3)
            quit()
    if deathpoints == len(word):
        realdeathpoints += 1
        print(f"Nothing is correct. You get 5 chances. You have {5-realdeathpoints} chances left.")
        if realdeathpoints == 1:
            print("""
                  ----------
                  |    |
                  |    |
                  |    O
                  |
                  |
                  |""")
            time.sleep(3)
        elif realdeathpoints == 2:
            print("""
                  ----------
                  |    |
                  |    |
                  |    O
                  |    |
                  |
                  |""")
            time.sleep(3)
        elif realdeathpoints == 3:
            print("""
                  ----------
                  |    |
                  |    |
                  |   \O/
                  |    |
                  |
                  |""")
            time.sleep(3)
        elif realdeathpoints == 4:
            print("""
                  ----------
                  |    |
                  |    |
                  |   \O/
                  |    |
                  |   / \\
                  |""")
            print("Not dead yet!!!")
            time.sleep(3)
        if realdeathpoints == 5:
            print("You have failed.")
            time.sleep(3)
            quit()
    deathpoints = 0
    for z in userinputword:
        if z != "_":
            num += 1
    if num == len(word):
        print("Great Job!")
        time.sleep(3)
        quit()
    else:
        num = 0
