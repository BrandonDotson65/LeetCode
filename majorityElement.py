def majorityElement(numbersList):
    dictionary = {}
    for num in numbersList:
        if num in dictionary:
            dictionary[num] += 1
        else:
            dictionary[num] = 1
    majority = 0
    majorityElement = 0
    for values in dictionary.keys():
        if (dictionary[values] > majority):
            majority = dictionary[values]
            majorityElement = values
    return majorityElement

nums = [2,2,1,1,1,2,2]

print(majorityElement(nums))

def majorityElement2(numbersList):
    dictionary = {}
    for num in numbersList:
        if num in dictionary:
            dictionary[num] += 1
        else:
            dictionary[num] = 1
        if dictionary[num] > len(numbersList)/2:
            return num

nums = [2,2,1,1,1,2,2]

print(majorityElement2(nums))