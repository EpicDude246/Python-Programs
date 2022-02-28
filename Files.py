file = open(r"C:\Users\rjajoo\Desktop\Python\Files\The_Funeral_for_the_Origanal_File.txt", "a")


file.writelines(":( Pay your respects...")

file = open(r"C:\Users\rjajoo\Desktop\Python\Files\The_Funeral_for_the_Origanal_File.txt", "r+")
print(file.readlines())
