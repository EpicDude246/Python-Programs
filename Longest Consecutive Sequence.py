def longestConsecutive(input1):
    input1 = set(input1)
    longestSequence = 0
    for item in input1:
        if item-1 not in input1:
            x = 0
            while item in input1:
               item+=1
               x+=1
               longestSequence = max(longestSequence,x)
    return longestSequence
e = input('input ').split()
input1 = []
[input1.append(int(x)) for x in e]
print(longestConsecutive(input1))