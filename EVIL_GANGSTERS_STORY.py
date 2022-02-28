import random
try:
    import names
except:
    warn = True
more = "Yes"
ca = ""
r1 = random.randint(10, 40)
gangsters = 41
cars = int(gangsters / 4)
bought = []


def bank(x, y):
    if cash <= 0:
        print(f"THE END!!!!!!!! You went bankrupt with ${x} and killed {30 - y} gangsters.")
        quit()


cash = random.randint(1000000, 10000000)
if warn == False:
    evil_guy_name = names.get_first_name(gender='male')
else:
    evil_guy_name = "Bob"
name = input("What is your name? ")
if name.lower() == "reyansh":
    print("Hi creator!!!")
print(f"""Hello {name}.
You are on a mission. 
You may live and get lots of rewards. You may die or face severe consequences.
Explore all the endings! Have fun!!!!!""")

print(f"""You were a rich and mighty businessman.
You had ${cash}.
One day a guy named {evil_guy_name} came to your door.
He had a gun in his hand and he told you to give him {cash} dollars.""")

cha = input("What would you do? Run, get in the car, or get your gun? A, B, or C? ")

if cha.upper() == "C":
    print(f"""You get your gun.
{evil_guy_name} calls his bodyguards and they knock you out.
{evil_guy_name} shoots your head and takes your {cash} dollars.
THE END!!!!!!!!!! 
You died with ${cash} and killed {41 - gangsters} gangsters.""")
    quit()
if cha.upper() == "A":
    print(f"""You run away and go to the closest house near you and hide. 
The robbers see you go and they come inside the house.
They kill the old lady but still could not find you so they leave and take all the valuables with them
Then, you leave the house and go to somewhere else""")

    ca = input("What would you do? Decide to stay here, try to leave the state, or fight them. A, B, C?")
if ca.upper() == "C":
    print(f"""You get your gun and try to find them. 
They shoot you and shoot right at you.
You dodge the bullet but eventually they hit your knee and you fall to the ground.
They shoot you and take all your personal belongings and run away
You died with ${cash} and killed {41 - gangsters} gangsters""")
    quit()
if ca.upper() == "A":
    print(f"""You decide to stay here and not escape from danger.
You spotted {evil_guy_name} and kill {41 - gangsters} gangsters.
But {evil_guy_name} and his gangsters find you and this time hang you and torture you.
Sadly, the torturing was too hard and you were hanged to death.
You died with ${cash} and killed {41 - gangsters} gangsters """)
    quit()
if ca.upper() == "B":
    print(f"""You get ready to escape from the state.
Even though some of the gangsters are guarding the borders you find a path which they are not guarding.
You get in your car and drive through the border.
You have 2 AK-47's with you in case you spot the gangsters.
After a 100 miles of driving you spot {gangsters} gangsters and you kill them
You spot the rest of the gang and kill  gangsters
There was only {42 - gangsters} gangster left and he was their leader
You barely killed him and cross the border and live in freedom
You win with ${cash} and you killed {gangsters} gangsters
You saved the world!!!!!!!""")
    quit()
if cha.upper() == "B":
    print(f"""You run and get the keys to your car.
You distract {evil_guy_name} and you lose him.
You get in your car and speed away to the police station
The police officers say that {evil_guy_name} has been roaming around terrorizing innocent people
They are all over the state.
We need someone rich, smart, and powerful to solve the problem.
We will give you a reward if you succeed
Are you up to the challenge?""")
    ba = input("Yes or No? ")
    if ba.lower() == "no":
        print(f"""Fine, the policeman says. ☹.""")
        print(f"""The robbers and {evil_guy_name} come back to your house. You are unprepared and they shoot you down. 
                                THE END!!!!!!!! You died with ${cash} and killed {41 - gangsters} gangsters..""")
        quit()
    if ba.lower() == "yes":
        print(f"""The cop asks what mode of transportation would you like? 
    You have {cash} dollars to work with. """)
        transport = input("Jet - $199999, speedy car (type in car)- $29000, or bike - $400 ")
        gun = input("Do you want a gun? Yes or no? It costs $10000 because of its epicness. ")
        if gun.lower() == "yes":
            cash -= 100000

    if transport.lower() == "bike":
        cash -= 400
        if gun.lower() == "no":
            print(f"""The gangsters catch up with you in their car. They shoot you.
        You died with ${cash} and killed {41 - gangsters} gangsters.""")
            quit()
        if gun.lower() == "yes":
            gangsters -= 10
            print(f"""The gangsters catch up with you in their car. You take your gun and start shooting them. 
        You took down 10 with your epic gun but they ended up killing you.
        THE END!!!!!!!! You died with ${cash} and killed {41 - gangsters} gangsters.""")
        quit()
    if transport.lower() == "jet":
        while cars > 0:
            bank(cash, gangsters)
            print(f"You jumped in your jet. The gangsters follow you on foot. Do you want grenades?")
            grenades = input("Yes or no? They cost $9999 each?")
            print(f"You have {cash} cash to work with.")
            if grenades.lower() == "yes":
                grenades_quantity = int(input("How many?"))
                cash -= 9999 * grenades_quantity
                bank(cash, gangsters)
                if grenades_quantity >= 4:
                    grenades_quantity = 4
                print(f"""You fly near the gangsters. You grenade their {grenades_quantity} car(s).""")
                cars -= grenades_quantity
        if cars == 0:
            print(f"THE END!!!!!!!! You saved the world with ${cash} remaining and killed {gangsters} gangsters")
            quit()
    if transport.lower() == "car":
        cash -= 29000
        gangsters -= 10
        print(f"""You hop into your car and rush away from the city. You are surprised to see gangsters behind 
    you and you shoot them, killing {51 - gangsters} before they gain on you. You slam the gas and you rush out very 
fast. You go to a store where you can buy stuff.""")
    while more.lower() == "yes":
        bought.append(input("Do you want to buy a bazooka - $ 100000, some food - $40, or water? - $1").lower())
        print(f"You have ${cash} to work with.")
        more = input("More? Yes or no?")
    bank(cash, gangsters)
    water_amount = bought.count("water")
    food_amount = bought.count("food")
    bazooka_amount = bought.count("bazooka")
    cash -= bazooka_amount * 100000
    cash -= water_amount
    cash -= food_amount * 40
    if water_amount == 0:
        print(f"""You get out of the the store and then you remembered you forgot water.
    Sadly you can't go back to the store.
    You ate your food.
    After a few days, you dehydrate and die without water
    THE END!! You died with ${cash} and you killed {51 - gangsters} gangsters""")
    quit()
    if food_amount == 0:
        print(f"""You get out of the the store and then you remembered you forgot food.
    Sadly you can't go back to the store.
    You drink your water.
    After a couple days, you die of starvation without food
    THE END!!!!! You died with ${cash} and you killed {51 - gangsters} gangsters""")
    quit()
    if bazooka_amount == 0:
        print(f"""You get out of the the store and then you remembered you forgot bazooka's.
    Sadly you can't go back to the store.
    You drink your water and eat your food.
    The gangsters find you and you have nothing to fight them and they kill you.
    THE END!!!!!!! You killed {51 - gangsters} gangsters and they took your {cash} dollars""")
        quit()
    if bazooka_amount > 0 and food_amount > 0 and water_amount > 0:
        print(f"""You race away in you vehicle and use your bazooka(s) to shoot the {gangsters} gangsters, you eat 
    your food, 
    and you drink your water. 
    You go somewhere you can live in freedom
    YOU DON'T GET REWARD!!!!
    THE END!!!! You win with ${cash} and you killed {gangsters} gangsters""")
