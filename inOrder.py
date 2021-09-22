# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inOrder(treeNode):
    
    if treeNode:
        return inOrder(treeNode.left) + [treeNode.val] + inOrder(treeNode.right)
    else:
        return []

testNode = TreeNode(1)

testNode.right = TreeNode(2)
testNode.right.left = TreeNode(3)

#print(inOrder(testNode))

testNode2 = TreeNode(1)

testNode2.left = TreeNode(2)

print(inOrder(testNode2))