def removeElement(nums, val):
    matching = 0
    for item in nums:
        if item == val:
            matching += 1
    return len(nums) - matching

def removeElement2(nums, val):
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return i

numberList = [0,1,2,2,3,0,4,2]
numberList2 = [3,2,2,3]

print(removeElement(numberList2, 3))
print(removeElement2(numberList2, 3))
#print(numberList2)



