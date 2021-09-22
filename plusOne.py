# You are given a large integer represented as an integer array digits, where 
# each digits[i] is the ith digit of the integer. The digits are ordered from 
# most significant to least significant in left-to-right order. The large integer 
# does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

def plusOne(numberList):
    if len(numberList) == 1 and numberList[0] == 9:
        return [1, 0]
    elif numberList[-1] != 9:
        numberList[-1] += 1
        return numberList
    else:
        numberList[-1] = 0
        numberList[:-1] = plusOne(numberList[:-1])
        return numberList

numList = [1, 2, 3]
numList2 = [4, 3, 2, 1]
numList3 = [7, 6, 2, 9]

print(plusOne(numList3))