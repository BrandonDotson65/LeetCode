def generateParenthesis(n):
    if n == 0: return []
    left, right, res = n, n, []
    dfs(left, right, res, "")
    return res

def dfs(left, right, res, string):
    if right < left:
        return
    if not left and not right:
        res.append(string)
        return
    if left:
        dfs(left-1, right, res, string + "(")
    if right:
        dfs(left, right-1, res, string + ")")

print(generateParenthesis(4))