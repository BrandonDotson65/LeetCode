def isValid(string):
    stack = []
    dictionary = {"}": "{", ")": "(", "]":"["}
    for letter in string:
        if letter in dictionary.values():
            stack.append(letter)
        elif letter in dictionary.keys():
            if stack == [] or dictionary[letter] != stack.pop():
                return False
        else:
            return False

    return stack == []

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(){]"))