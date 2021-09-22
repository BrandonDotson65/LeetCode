# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest 
# sum and return its sum.
# A subarray is a contiguous part of an array.

def maxSubArray(numList):
    if len(numList) == 0:
        return 0
    currSum = maxSum = numList[0]

    for num in numList[1:]:
        currSum = max(num, currSum + num)
        maxSum = max(maxSum, currSum)
    
    return maxSum

numberList = [-2,1,-3,4,-1,2,1,-5,4]
numberList2 = [1]
numberList3 = [5,4,-1,7,8]

print(maxSubArray(numberList3))