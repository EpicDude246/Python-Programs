
def LongestSubstring(input1):
    x = 0
    y = 0
    d = {}
    answer = 0
    while y < len(input1):
        if input1[y] not in d or x>d[input1[y]]:
            answer = max(answer,(y-x+1))
            d[input1[y]] = y
        else:
            x = d[input1[y]]+1
            answer = max(answer,(y-x+1))
            y-=1
        y+=1
        print(d)
    return answer
print(LongestSubstring(input('input ')))