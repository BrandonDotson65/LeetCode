def removeDuplicates(numList):
    duplicates = 0
    prev = None
    for num in numList:
        if prev is not None and num == prev:
            duplicates += 1
        prev = num
    return len(numList) - duplicates

numberList = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(numberList))