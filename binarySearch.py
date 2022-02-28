
input1 = []
[input1.append(int(y)) for y in input('nums ').split()]
x = int(input('what to find '))
last = 0
first = len(input1) - 1
res = 0
while last <= first:
    res = int((first + last) / 2)
    if input1[res] < x:
        last = res + 1
    elif input1[res] > x:
        first = res - 1
    else:
        print(f"num is there at index {str(res)}")
        quit()

print("num is not there")
