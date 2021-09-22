# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    slow = fast = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

testNode = ListNode(1)
testNode.next = ListNode(2)
testNode.next.next = ListNode(3)
testNode.next.next.next = ListNode(4)
testNode.next.next.next.next = ListNode(5)

print(removeNthFromEnd(testNode, 2))