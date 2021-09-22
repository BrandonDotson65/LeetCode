# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if root:
        return 1 + max(maxDepth(root.left), maxDepth(root.right))
    else:
        return 0

testNodes = TreeNode(1)
testNodes.left = TreeNode(2)
testNodes.left.left = TreeNode(3)
testNodes.left.right = TreeNode(5)
testNodes.right = TreeNode(2)

print(maxDepth(testNodes))