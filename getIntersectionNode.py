class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA, headB):
    tempSet = set()
    while headA and headB:
        if headA == headB:
            return headA
        if headA in tempSet:
            return headA
        elif headB in tempSet:
            return headB
        tempSet.add(headA)
        tempSet.add(headB)
        headA = headA.next
        headB = headB.next
    while headA:
        if headA in tempSet:
            return headA
        tempSet.add(headA)
        headA = headA.next
    while headB:
        if headB in tempSet:
            return headB
        tempSet.add(headB)
        headB = headB.next
    return None

#testNode2 = ListNode(3)
#testNode2.next = ListNode(4)

#testNode = ListNode(1)
#testNode.next = ListNode(3)
#testNode.next.next = ListNode(5)
#testNode.next.next.next = testNode2

#testNode3 = ListNode(3)
#testNode3.next = testNode2

#print(getIntersectionNode(testNode, testNode3).next.val)

testNode = ListNode(1)
testNode.next = ListNode(2)

testNode2 = ListNode(1)
testNode2.next = ListNode(2)

testNode3 = ListNode(4)
testNode3.next = ListNode(5)

testNode.next.next = testNode3
testNode2.next.next = testNode3

print(getIntersectionNode(testNode, testNode2).val)