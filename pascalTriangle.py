def generate2(numRows):
    pasc = [[1] * (i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1, i):
            pasc[i][j] = pasc[i-1][j-1] + pasc[i-1][j]
    
    return pasc

print(generate2(5))