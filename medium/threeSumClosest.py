def threeSumClosest(nums, target):
    res = nums[0] + nums[1] + nums[2]
    nums.sort()
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            temp = nums[i] + nums[left] + nums[right]
            if temp == target:
                return temp
            if abs(temp - target) < abs(res - target):
                res = temp
            if temp < target:
                left += 1
            elif temp > target:
                right -= 1
    return res

nums = [-1,2,1,-4]

print(threeSumClosest(nums, 1))