#algorithm based on https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
def nextPermutation(nums: list):
    i = j = n = len(nums) - 1
    #find suffix
    while i > 0 and nums[i - 1] >= nums[i]:
        i -= 1
    if i == 0:
        nums.reverse()
        return
    #pivot point
    k = i - 1
    #find right most successor to pivot
    while nums[j] <= nums[k]:
        j -= 1
    #swap
    temp = nums[j]
    nums[j] = nums[k]
    nums[k] = temp
    #reverse suffix
    while i < n:
        temp = nums[n]
        nums[n] = nums[i]
        nums[i] = temp
        i += 1
        n -= 1
    return

numbers = [1, 2, 5, 3, 3, 0]

nextPermutation(numbers)
print(numbers)