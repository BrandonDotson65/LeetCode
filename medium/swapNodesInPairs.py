#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapNodesInPairs(head):
    dummy = prev = ListNode(0)
    dummy.next = prev.next = head
    if head is None: return None
    while prev.next and prev.next.next:
        a = prev.next
        b = a.next
        prev.next = b
        a.next = b.next
        b.next = a
        prev = a

    return dummy.next
    
testNode = ListNode(1)
testNode.next = ListNode(2)
testNode.next.next = ListNode(3)
testNode.next.next.next = ListNode(4)

print(swapNodesInPairs(testNode).next.next.next.val)
