def isPalindrome(string):
    newString = ""
    for letter in string:
        if (ord(letter) < 97 or ord(letter) > 122) and (ord(letter) < 65 or ord(letter) > 90 ):
            continue
        else:
            newString += letter
    newString = newString.lower()
    return newString == newString[::-1]


def isPalindrome2(s):
    beg, end = 0, len(s) - 1
    while beg <= end:
        while not s[beg].isalnum() and beg < end: beg += 1
        while not s[end].isalnum() and beg < end: end -= 1
        if s[beg] == s[end] or s[beg].upper() == s[end].upper():
            beg, end = beg + 1, end - 1
        else:
            return False
        return True

print(isPalindrome("A man, a plan, a canal: Panama"))