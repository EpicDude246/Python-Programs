
inputList = input('Input the tepratures followed by spaces. ').split()

n = len(inputList)

days = [-1] * n
stack = []
finalList = []

for num in range(n):
    while (len(stack)) != 0 and (inputList[stack[-1]] < inputList[num]):
        days[stack[-1]] = num - stack[-1]
        stack.pop(-1)
    stack.append(num)

for num in range(n):
    if days[num] > 0:
        finalList.append(days[num])
    else:
        finalList.append(0)

print(finalList)
