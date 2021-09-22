# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sameTree(treeOne, treeTwo):
    if treeOne and treeTwo:
        if treeOne.val == treeTwo.val:
            return (sameTree(treeOne.left, treeTwo.left) and sameTree(treeOne.right, treeTwo.right))
        else:
            return False
    elif treeOne or treeTwo:
        return False
    else:
        return True
    
treeNode1 = TreeNode(1)
treeNode1.left = TreeNode(2)
treeNode1.right = TreeNode(4)

treeNode2 = TreeNode(1)
treeNode2.left = TreeNode(2)
treeNode2.right = TreeNode(4)

print(sameTree(treeNode1, treeNode2))
