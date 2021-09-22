def myAtoi(string):
    res = 0
    symbol = 1
    if len(string) == 0: return 0
    for i, letter in enumerate(string):
        if letter == ' ':
            continue
        elif letter == '-':
            symbol = -1
        elif letter == '+':
            continue
        elif ord(letter) < 48 or ord(letter) > 57:
            return 0
        else:
            while i < len(string) and ord(string[i]) > 47 and ord(string[i]) < 58:
                res = res * 10 + ord(string[i]) - ord('0')
                i += 1
            return max(-2**31, min(symbol * res, 2**31-1))

testString = "   -42"
testString2 = "         4193 with words"
testString3 = "there is words 28901"
testString4 = ""

def myAtoi2(s):
    """
    :type str: str
    :rtype: int
    """
    ###better to do strip before sanity check (although 8ms slower):
    #ls = list(s.strip())
    #if len(ls) == 0 : return 0
    if len(s) == 0 : return 0
    ls = list(s.strip())
    sign = -1 if ls[0] == '-' else 1
    if ls[0] in ['-','+'] : del ls[0]
    ret, i = 0, 0
    while i < len(ls) and ls[i].isdigit() :
        ret = ret*10 + ord(ls[i]) - ord('0')
        i += 1
    return max(-2**31, min(sign * ret,2**31-1))

print(myAtoi(testString4))