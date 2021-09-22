class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(intArray):
    length = len(intArray)
    mid = length // 2
    if length % 2 == 0: mid -= 1
    left = right = root = TreeNode(intArray[mid])
    decreasing, increasing = mid - 1, mid + 1
    while decreasing > -1 and increasing < length:
        left.left = TreeNode(intArray[decreasing])
        right.right = TreeNode(intArray[increasing])
        left, right = left.left, right.right
        decreasing -= 1
        increasing += 1
    if increasing < length: right.right = TreeNode(intArray[increasing])
    return root

def sortedArrayToBST2(intArray):
    if not intArray:
        return None
    mid = len(intArray) // 2
    node = TreeNode(intArray[mid])
    node.left = sortedArrayToBST2(intArray[:mid])
    node.right = sortedArrayToBST2(intArray[mid+1:])
    return node

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numberList2 = [1, 2, 3, 4, 5]

rootNode = sortedArrayToBST2(numberList)
print(rootNode.left.val)
print(rootNode.val)
#rootNode2 = sortedArrayToBST(numberList2)
#print(rootNode.val)
#print(rootNode.right.val)
#print(rootNode.right.right.val)
#print(rootNode.right.right.right.val)
#print(rootNode.right.right.right.right.val)
#print(rootNode.right.right.right.right.right.val)

#print(rootNode2.val)
#print(rootNode2.left.val)
#print(rootNode2.left.left.val)
#print(rootNode2.right.val)
#print(rootNode2.right.right.val)

