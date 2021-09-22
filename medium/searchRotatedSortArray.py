#my solution
def search(nums: list, target: int):
    answer, idx = 0, 0
    while nums[idx] < nums[idx + 1]:
        idx += 1
    subArr1, subArr2 = nums[:idx+1], nums[idx+1:]
    if target >= subArr1[0] and target <= subArr1[len(subArr1) - 1]:
        answer = binarySearch(subArr1, target)
    elif target <= subArr2[len(subArr2) - 1]:
        answer = len(subArr1) + binarySearch(subArr2, target)
    else: return -1
    return answer

def binarySearch(nums, target):
    beg, end = 0, len(nums)
    while beg < end:
        mid = beg + end // 2
        if target < nums[mid]:
            end = mid
        elif target > nums[mid]:
            beg = mid
        elif target == nums[mid]:
            return mid

testArray = [3, 4, 5, 1, 2]
nums = [4,5,6,7,0,1,2]

#print(search(nums, 3))

#another solution
def search2(nums: list, target: int):
    if nums is None:
        return -1
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        if nums[low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1

print(search2(nums, 6))
