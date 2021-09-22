class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(node, targetSum):
    if not node:
        return False
    elif not node.left and not node.right and node.val == targetSum:
        return True
    targetSum -= node.val
    return hasPathSum(node.left, targetSum) or hasPathSum(node.right, targetSum)

testNodes = TreeNode(5)
testNodes.left = TreeNode(4)
testNodes.left.left = TreeNode(11)
testNodes.left.left.right = TreeNode(2)
testNodes.left.left.left = TreeNode(7)

testNodes.right = TreeNode(8)
testNodes.right.right = TreeNode(4)
testNodes.right.left = TreeNode(13)
testNodes.right.right.right = TreeNode(1)

print(hasPathSum(testNodes, 22))