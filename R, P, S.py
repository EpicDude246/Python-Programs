import random

print("""This is a Rock Paper Scissors game.
This is how to play.
Rock and paper - Paper wins.
Scissors and paper - Scissors wins.
Rock and scissors - Rock wins.""")


def RPSFunction(Your_Choice, y):
    l=""
    Your_Choice = Your_Choice.upper()
#tie
    if Your_Choice == y:
        l="t"
#rock    
    if Your_Choice =="S" and y =="R":
        l="l"
    if Your_Choice =="S" and y =="P":
        l="w"
#paper    
    if Your_Choice =="R" and y =="S":
        l="w"
    if Your_Choice =="R" and y =="P":
        l="l"
#scissors
    if Your_Choice =="P" and y =="R":
        l="w"
    if Your_Choice =="P" and y =="S":
        l="l"
#Wrong input
    if l=="":
        print(Your_Choice, "is not a correct input.")
    return l


continuer = "yes"
RPSFunctionResult = ""
z = ""
you = ""
while continuer.lower() == "yes":
    bot = random.choice(["R", "P", "S"])
    you = input(" Are you R, P, or S? ")

    RPSFunctionResult = RPSFunction(you, bot)

    z = f"bot - {bot}, you - {you} "

    if RPSFunctionResult == "l":
        print(f"You lost! {z}")

    elif RPSFunctionResult == "w":
        print(f"You won! {z}")

    elif RPSFunctionResult == "t":
        print(f"You tied! {z}")
    else:
	continue
    continuer = input("Would you like to continue? Yes or no?")
print("BYE!!!")