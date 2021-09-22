def isPalindrome(integer):
    if (integer < 0):
        return False
    temp = str(integer)
    integer = int(temp[::-1])
    return True if int(temp) == integer else False

print(isPalindrome(121))