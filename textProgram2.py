s = input("Type sting here ------>  ")
for x in range(len(s)):
    if x != 0:
        print(s[-x], end="")
print(s[0])
