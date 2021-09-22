def getRow(index):
    pasc = [[1] * (i+1) for i in range(index+1)]
    for i in range(index+1):
        for j in range(1, i):
            pasc[i][j] = pasc[i-1][j-1] + pasc[i-1][j]
        if i == index:
            return pasc[i]

print(getRow(6))
        
