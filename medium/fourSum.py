def fourSum(numsList: list, target: int):
    numsList.sort()
    length = len(numsList)
    seen = set()
    answr = set()
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                s = target - numsList[i] - numsList[j] - numsList[k]
                if s in seen:
                    arr = sorted([numsList[i], numsList[j], numsList[k], s])
                    answr.add((arr[0], arr[1], arr[2], arr[3]))
        seen.add(numsList[i])
    return answr

nums = [1,0,-1,0,-2,2]
target = 0

print(fourSum(nums, target))
            