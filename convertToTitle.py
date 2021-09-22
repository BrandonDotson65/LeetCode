def convertToTitle(colNum):
    result = []
    characters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    while colNum > 0:
        result.append(characters[(colNum - 1) % 26])
        colNum = (colNum - 1) // 26
    return "".join(reversed(result))

print(convertToTitle(18400))