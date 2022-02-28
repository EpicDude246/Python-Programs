def find3Numbers(A):
    for j in range(len(A)):
        if (curr_sum - A[j]) in s:
            print("Triplet is",
                    ", ", A[j], ", ", curr_sum-A[j])
            return True
     
    return False
print(find3Numbers(input('list')))