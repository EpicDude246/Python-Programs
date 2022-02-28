def findNums(l):
    A = []
    [A.append(int(x)) for x in l]
    for i in range(len(A)-1):
        s = set()
        curr_sum = 0 - A[i]
        for j in range(i + 1, len(A)):
            if (curr_sum - A[j]) in s:
                print(f"The triplet is {A[i]}, {A[j]}, and {curr_sum-A[j]}")
                quit()
            s.add(A[j])
    print('none')


findNums(input('list ').split())