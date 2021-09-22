def intToRoman(integer):
    if integer <= 0: return ""
    dictionary = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
    prev = 1
    res = ""
    for key in dictionary.keys():
        if integer > key:
            if integer > 1000:
                carry = integer // 1000
                res += dictionary[1000] * carry
                return res + intToRoman(integer - 1000*carry)
            prev = key
        else:
            if (integer == key): return dictionary[key]
            carry = integer // prev
            res += dictionary[prev]*carry
            return res + intToRoman(integer - prev*carry)

print(intToRoman(56))

