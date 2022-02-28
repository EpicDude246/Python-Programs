import random
try:
    print("Welcome to the Guessing Game!\n\n\n")
    x = 0
    
    while True:
        parameter = int(input("What will be the highest number? "))
        print("\n")
        if (parameter < 9 or 50 < parameter):
            print("This num is not acceptable.\n")
            continue
            
        print("The lowest number is 1. ")
        break
        
    numToGuess = random.randint(1, parameter)
    while True:
        x += 1
        guess = int(input("What will be the guess? "))
        print("\n")
        
        if guess == numToGuess:
            print("You won!!")
            quit()
        
        if numToGuess > guess and numToGuess < guess + 5:
            print("You are close! ")
            
        else:
            print("You are far!")
        if x == 10:
            break
            
    print("""                 .d888 
                    d88P"  
                    888    
     .d88b.  .d88b. 888888 
    d88""88bd88""88b888    
    888  888888  888888    
    Y88..88PY88..88P888    
     "Y88P"  "Y88P" 888 """)

except:
    print("(•̀o•́),ง")
    print("Sorry, the game FAILED. Please try again.")