class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preOrderTraversal(root):
    if not root:
        return []
    else:
        return [root.val] + preOrderTraversal(root.left) + preOrderTraversal(root.right)

rootNode = TreeNode(1)
rootNode.right = TreeNode(2)
rootNode.right.left = TreeNode(3)

print(preOrderTraversal(rootNode))