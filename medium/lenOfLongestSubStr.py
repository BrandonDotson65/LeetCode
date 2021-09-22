def lengthOfLongestSubString(string):
    if not string:
        return 0
    s = set()
    currMax = 0
    for letter in string:
        if letter in s:
            currMax = max(currMax, len(s))
            s.clear()
        else:
            s.add(letter)
    return max(currMax, len(s))

print(lengthOfLongestSubString("pwwkew"))
print(lengthOfLongestSubString("abcabcbb"))
print(lengthOfLongestSubString("bbbbb"))