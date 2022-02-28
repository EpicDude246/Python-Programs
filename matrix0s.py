inputMatrix = [[0,1,1,1],[1,1,1,1],[1,1,0,1]]
change = []
otherMatrix = inputMatrix.copy()

for i in range(len(inputMatrix)):
    for n in range(len(inputMatrix[i])):
        if inputMatrix[i][n] == 0:
            change.append(n)
            otherMatrix[i] = [0]*len(inputMatrix[i])

for i in range(len(inputMatrix)):
    for n in range(len(inputMatrix[i])):
        if n in change:
            otherMatrix[i][n] = 0


print('\n'.join(['\t'.join([str(c) for c in row])
      for row in otherMatrix]))

'''
Runtime: 2NM
Space: NM+M
'''
