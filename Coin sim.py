import random

def coiny(range1, range2):
    x = random.randint(range1, range2)
    return x
    
    
range1 = int(input("range1? "))
range2 = int(input("range2? "))
players = int(input("Players? "))
play = random.randint(1, players)
z = ""
x = True


print("In the pause, type no to stop. ")


while x:
    if play == players + 1:
        play = 1
        
        
    rollq = input("Want to roll? ")
    
    
    if rollq.lower() == "yes":
        coin = coiny(range1, range2)
        print("Roll is " + str(coin) + ". Player was " + str(play))
        
        
    z = input()
    
    if z.lower() == "no":
        x = False