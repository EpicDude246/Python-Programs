from os import listdir
import random
from os.path import isfile, join
cats = listdir(r"C:\Users\rjajoo\Desktop\Python\Bot\images")
print(cats)
cat = random.choice(cats)
catpath = r"C:\Users\rjajoo\Desktop\Python\Bot\images" + cat
print(file = catpath)
