import os
x = 0

print("""++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
""")
input1 = input(r"Please tell the name of the file like The_Funeral_for_the_Origanal_File.txt.")


print("")
print("")
input1 = r"C:\Testfile\\" + str(input1)


print("Here are all the files.")
for file in os.listdir("C:\Testfile\\"):
    x += 1
    if file.endswith(".txt"):
        print(os.path.join(str(x), "C:\Testfile\\", file))
print("")
print("")


file = open(input1, "a")
file.close()
while True:
    print("\n ---------------------------------------------------------------------------------------------------------------------------")
    print("""What would you like to do with the file?
1 - Read
2 - Replace
3 - Delete
4 - Add
5 - Clear
6 - Stop
""")
    
    whattodo = input("Please enter your choice: ")
    whattodo = whattodo.lower()
    if whattodo == "6":
        break

    elif whattodo == "5":
        file = open(input1, "w")
        file.write("")
        file.close()
        
    elif whattodo == "4":
        file = open(input1, "a")
        whattoap = input("What should I append?")
        file.write(whattoap)
        file.close()
        
    elif whattodo == "2":
        file = open(input1, "w")
        whattore = input("What should I write?")
        file.write(whattore)
        file.close()
        
    elif whattodo == "1":
        file = open(input1, "r")
        print(file.read())
        file.close()
        
    elif whattodo == "3":
        os.remove(input1)


        while True:
            stop = input("Do you want to stop? Yes or no?")
            stop = stop.lower()
            if stop == "yes":
                print("Ok.")
                quit()
                
            elif stop == "no":
                print("Ok.")
                break
            
            else:
                print("Try again")
                continue



        input1 = input("Your file has been deleted. I will need a new name.") + ".txt"
        input1 = r"C:\Testfile\\" + str(input1)
        file = open(input1, "a")
        file.close()
        
    else:
        print("This is not a command.")
        continue
    
print("Bye!")

