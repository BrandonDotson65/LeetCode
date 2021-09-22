def romToInt(romanString):
    dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    # set last to 9999 to prevent if 
    # statement from running on first 
    # iteration (last letter variable is null)
    curr, last = 0, 9999
    lastLetter, currLetter = None, None
    for letter in romanString:
        curr = dictionary[letter]
        currLetter = letter
        if (curr > last):
            total += dictionary[currLetter] - dictionary[lastLetter] - dictionary[lastLetter]
        else:
            total += dictionary[letter]

        lastLetter = currLetter
        last = curr
    
    return total

print(romToInt("XC"))