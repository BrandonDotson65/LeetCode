nums = [2, 7, 11, 15]
target = 9

def twoSum(nums, target):
    dict = {}
    for i, n in enumerate(nums):
        num = target - n
        if num in dict:
            return [dict[num], i]
        else:
            dict[n] = i

mainList = twoSum(nums, target)

print(mainList)