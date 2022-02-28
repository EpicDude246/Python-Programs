nums = []
[nums.append(int(x)) for x in input('nums with spaces between ').split()]
k = int(input('k '))
dic = {}
a = count = 0
for num in nums:
    a += num
    if a == k:
        count += 1
    if a - k in dic:
        count += dic[a-k]
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
print(count)
