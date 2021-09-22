class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(node):
    if not node:
        return 0
    elif not node.left:
        return 1 + minDepth(node.right)
    elif not node.right:
        return 1 + minDepth(node.left)
    return 1 + min(minDepth(node.left), minDepth(node.right))

testNodes = TreeNode(2)
testNodes.left = TreeNode(1)
testNodes.right = TreeNode(3)
testNodes.right.right = TreeNode(5)
testNodes.right.left = TreeNode(4)

print(minDepth(testNodes))
