def maxSubArray(nums):
    sum1 = 0
    retunNum = 0
    for i in nums:
        sum1 = max(0, sum1) + i
        retunNum = max(retunNum, sum1)
    return max(nums) if retunNum == 0 else retunNum

e = input('input ').split()
input1 = []
[input1.append(int(x)) for x in e]
print(maxSubArray(input1))