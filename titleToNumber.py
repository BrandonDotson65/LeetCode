def titleToNumber(columnTitle):
    integers = [i for i in range(1, 27)]
    index, result = 0, 0
    for i, letter in enumerate(reversed(columnTitle)):
        index = ord(letter) - 65
        if i == 0:
            result += integers[index]
        else:
            result += integers[index]*(26**i)
    return result

#print(titleToNumber("FXSHRXW"))

def titleToNumber2(columnTitle):
    integers = [i for i in range(1, 27)]
    total = 0
    for i, letter in enumerate(reversed(columnTitle)):
        total += integers[ord(letter) - 65] * (26 ** i)
    return total

#print(titleToNumber2("FXSHRXW"))

