def singleNumber(numberList):
    integer = 0
    for num in numberList:
        integer ^= num
    return integer

numList = [4,1,2,1,2]

print(singleNumber(numList))