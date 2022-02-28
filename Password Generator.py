import random
import time
def password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def randls(w, nums, letters):
        uppercase = []
        [uppercase.append(x.upper()) for x in letters]
        ups = 0
        for x in letters:
            if random.choice(range(nums)) == 1:
                if random.choice([1, 2]):
                    w += x
                else:
                    w += x.upper()
                    ups +=1
        if ups < 2:
            w += uppercase[random.randint(0, 25)]
            w += str(random.randint(1, 9))
            w += uppercase[random.randint(0, 25)]
        return w
    while True:
        pw = ""
        pw = randls(pw, 9, letters)
        if random.choice([1, 2]) == 1:
            pw += str(random.randint(1, 9))
        pw += random.choice(["!", "@", "#", "$", "%", "&", "?"])+str(random.randint(1, 9))+random.choice(["!", "@", "#", "$", "%", "&", "?"])
        pw += str(random.randint(1, 9))
        if random.choice([1, 2]) == 1:
            pw += random.choice(["!", "@", "#", "$", "%", "&", "?"])
        pw = randls(pw, 8, letters)
        pw += str(random.randint(1, 9))
        if len(pw) > 12:
            if random.choice([1, 2]) == 1:
                pw = str(letters[random.randint(0, 25)])+pw[5:16]
            else:
                pw = str(letters[random.randint(0, 25)]).upper()+pw[5:16]
        print(pw)
        time.sleep(2)

password()
