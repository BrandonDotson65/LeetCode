def twoSum(numbersList, target):
    dictionary = {}
    for i, num in enumerate(numbersList):
        element = target - num
        if element in dictionary.keys():
            return [dictionary[element]+1, i+1]
        else:
            dictionary[num] = i
    return None

numbers = [2,7,11,15]
numbers2 = [2, 3, 4]
numbers3 = [-1, 0]

print(twoSum(numbers, 9))