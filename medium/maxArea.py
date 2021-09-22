def maxArea(heightList):
    left, right, width, res = 0, len(heightList) - 1, len(heightList) - 1, 0
    for w in range(width, 0, -1):
        if heightList[left] < heightList[right]:
            res, left = max(res, heightList[left] * w), left + 1
        else:
            res, right = max(res, heightList[right] * w), right - 1
    return res

height = [1,8,6,2,5,4,8,3,7]

print(maxArea(height))