def longestPalindromeSubStr(string):
    if len(string) == 0: return None
    if len(string) == 1: return string[0]
    if len(string) == 2: return string[0]
    currRes = ""
    res = ""
    dictionary = {}
    for i, letter in enumerate(reversed(string)):
        if string[i] == letter:
            currRes += letter
        else:
            if currRes: dictionary[currRes] = len(currRes)
            currRes = ""
    if currRes: dictionary[currRes] = len(currRes)        
    maxRes = 0
    for key in dictionary.keys():
        if dictionary[key] > maxRes:
            res = key
            maxRes = dictionary[key]
    return res

print(longestPalindromeSubStr("babbad"))

