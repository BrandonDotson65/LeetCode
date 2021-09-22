strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]

def commonPrefix(strList):
    result = ""
    for item in zip(*strList):
        if len(set(item)) == 1:
            result += item[0]
        else:
            return result
    return result
        
print(commonPrefix(strs))