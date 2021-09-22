def mergeArray(arrayOne, m, arrayTwo, n):
    while (m > 0 and n > 0):
        if arrayOne[m - 1] > arrayTwo[n - 1]:
            arrayOne[m + n - 1] = arrayOne[m - 1]
            m -= 1
        else:
            arrayOne[m + n - 1] = arrayTwo[n - 1]
            n -= 1
    if n > 0:
        arrayOne[:n] = arrayTwo[:n]

nums1 = [1,2,3,0,0,0]
nums2 = [2, 5, 6]

nums3 = [1, 1, 2, 0, 0, 0]
nums4 = [3, 3, 4]

nums5 = [0]
nums6 = [1]

nums7 = [4, 4, 5, 0, 0, 0]
nums8 = [1, 2, 2]

mergeArray(nums7, 3, nums8, 3)

print(nums7)