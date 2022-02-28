run = True
while run:
    string = input("What word/sentence do you want to search? ").lower()
    letters = {}
    for item in string:
        if item == " ":
            continue
        if item not in letters:
            letters[item] = 0
        letters[item] += 1
        
    for item in letters:
        print(f"{item}: {letters[item]}")
    print(len(string), "in total, counting all characters.")
    true = input("Would you like to do it again? Yes or No? ")
    if true.lower() == "no":
        run = False
