def addBinary(string1, string2):
    carry = 0
    result = ""

    list1 = list(string1)
    list2 = list(string2)

    while list1 or list2 or carry:
        if list1:
            carry += int(list1.pop())
        if list2:
            carry += int(list2.pop())
        
        result += str(carry % 2)
        carry //= 2
    
    return result[::-1]

tempString = "11"
tempString2 = "1"

tempString3 = "1010"
tempString4 = "1011"

print(addBinary(tempString, tempString2))
print(addBinary(tempString3, tempString4))