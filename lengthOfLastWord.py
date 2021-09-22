def lengthOfLastWord(string):
    length = 0
    for letter in reversed(string):
        if letter == " ":
            if length > 0:
                return length
        else:
            length += 1

testString = "   fly me   to   the moon  "

print(lengthOfLastWord(testString))