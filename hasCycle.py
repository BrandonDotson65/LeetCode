class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(headNode):
    dictionary = {}
    curr = headNode
    index = 0
    while curr:
        if (curr in dictionary.keys()):
            return True
        else:
            dictionary[curr] = index
            index += 1
            curr = curr.next
    return False
        

testNodes = ListNode(1)
testNodes.next = ListNode(3)
testNodes.next.next = ListNode(5)
testNodes.next.next.next = ListNode(8)
testNodes.next.next.next.next = ListNode(10)
testNodes.next.next.next.next.next = testNodes.next.next

print(hasCycle(testNodes))