class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def titleToNumber(columnTitle):
    result = 0
    integers = [i for i in range(1, 27)]
    for i, letter in enumerate(reversed(columnTitle)):
        result += integers[ord(letter) - 65]*(26**i)
    return result

print(titleToNumber("ZY"))

def isSymmetric(root):
    if not root:
        return False
    return (isSymmetricHelper(root.left, root.right))

def isSymmetricHelper(leftTree, rightTree):
    if leftTree and rightTree:
        if leftTree.val == rightTree.val:
            return isSymmetricHelper(leftTree.left, rightTree.right) and isSymmetricHelper(leftTree.right, rightTree.left)
        else:
            return False
    elif leftTree or rightTree:
        return False
    else:
        return True

def hasPathSum(node, targetSum):
    if not node:
        return False
    if not node.left and not node.right and node.val == targetSum:
        return True
    targetSum -= node.val
    return hasPathSum(node.left, targetSum) or hasPathSum(node.right, targetSum)
