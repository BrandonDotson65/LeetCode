class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postOrderTraversal(root):
    if not root:
        return []
    else:
        return postOrderTraversal(root.left) + postOrderTraversal(root.right) + [root.val]
    
rootNode = TreeNode(1)
rootNode.right = TreeNode(2)
rootNode.right.left = TreeNode(3)

print(postOrderTraversal(rootNode))