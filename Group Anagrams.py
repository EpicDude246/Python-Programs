
strs = ["eat","tea","tan","ate","nat","bat"]
answer = {}
for item in strs:
    x = str(sorted(item))
    if x in answer:
        answer[x].append(item)
    else:
        answer[x] = [item]
print(list(answer.values()))


'''
answer = set
for item in strings
x = the sorted string of item
if x in the final answer
add item to answer[x]
else replace answer[x] with [i]
return values of answer
'''