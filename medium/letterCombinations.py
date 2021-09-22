#discussion answer
def letterCombinations(digits: str):
    if not digits: return []
    digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', 
                    '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    result = ['']
    for idx in range(len(digits)):
        result = [prev + l for prev in result for l in digit_map[digits[idx]]]
    return result

#print(letterCombinations("23"))

#preferred method (depth first search + recursion)
def letterCombinations2(digits: str):
    digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', 
                    '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = []
    dfs(digit_map, digits, "", res)
    return res

def dfs(map, digits, path, res):
    if not digits:
        res.append(path)
        return
    for c in map[digits[0]]:
        dfs(map, digits[1:], path + c, res)

print(letterCombinations2("23"))