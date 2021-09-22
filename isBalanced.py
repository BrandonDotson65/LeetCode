class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBalanced(rootNode):
    if not rootNode:
        return True
    return (abs(findDepth(rootNode.left) - findDepth(rootNode.right)) <= 1)

def findDepth(node):
    if not node:
        return 0 
    return 1 + max(findDepth(node.left), findDepth(node.right))

testNodes = TreeNode(2)
testNodes.right = TreeNode(3)
testNodes.right.right = TreeNode(4)
#testNodes.right.right.right = TreeNode(5)
testNodes.left = TreeNode(1)

print(isBalanced(testNodes))