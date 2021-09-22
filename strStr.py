def strStr(haystack, needle):
    if needle == "":
        return 0
    length = len(needle)
    for i, letter in enumerate(haystack):
        if letter == needle[0]:
            if haystack[i:i + length] == needle:
                return i
    return -1

#made by somebody else, testing
def strStr2(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

print(strStr2("heell", "ll"))
print(strStr("heell", "ll"))

