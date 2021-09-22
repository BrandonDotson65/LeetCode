def searchRange(nums: list, target: int):
    left, right = 0, len(nums) - 1
    res = []
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            right = mid
            while mid - 1 >= 0 and nums[mid-1] == target:
                mid -= 1
            res.append(mid)
            while mid + 1 <= len(nums) - 1 and nums[right+1] == target:
                right += 1
            res.append(right)
            return res
        elif target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
    return [-1, -1]

nums = [5,7,7,8,8,10]
nums2 = []
target = 7

print(searchRange(nums, target))
