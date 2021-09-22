import math

def trailingZeroes(n):
    if n == 0:
        return 0
    numFactorial = math.factorial(n)
    trailZeroes = 0
    string = str(numFactorial)[::-1]
    for letter in string:
        if letter != "0":
            break
        trailZeroes += 1
    return trailZeroes

print(trailingZeroes(4))