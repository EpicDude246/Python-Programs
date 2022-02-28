def minDiff(l,k):
    result = float('inf')
    for i in range(len(l)-k+1):
        result = int(min(result, l[i+k-1] - l[i]))
    return result
 
 
list1 = [9,4,1,7]
list1.sort()
k = 3
  
print(minDiff(list1, k))

'''Sort the list, then find the minimum value among all k sized lists.'''