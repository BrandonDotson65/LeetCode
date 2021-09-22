# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSymmetricHelper(treeOne):
    return isSymmetric(treeOne.left, treeOne.right)

def isSymmetric(left, right):
    if left and right:
        if left.val == right.val:
            return isSymmetric(left.left, right.right) and isSymmetric(left.right, right.left)
        else:
            return False
    elif left or right:
        return False
    else:
        return True

testNodes = TreeNode(1)
testNodes.left = TreeNode(2)
testNodes.left.left = TreeNode(3)
testNodes.left.right = TreeNode(4)

testNodes.right = TreeNode(2)
testNodes.right.left = TreeNode(4)
testNodes.right.right = TreeNode(3)

print(isSymmetricHelper(testNodes))