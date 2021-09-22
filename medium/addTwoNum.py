class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNum(nodeOne, nodeTwo):
    carry = 0
    res = []
    while nodeOne or nodeTwo or carry:
        if nodeOne:
            carry += nodeOne.val
            nodeOne = nodeOne.next
        if nodeTwo:
            carry += nodeTwo.val
            nodeTwo = nodeTwo.next

        res.append(carry % 10)
        carry //= 10
    return res

list = [2, 4, 3]
list2 = [5, 6, 4]

testNodes1 = ListNode(9)
testNodes1.next = ListNode(9)
testNodes1.next.next = ListNode(9)
testNodes1.next.next.next = ListNode(9)
testNodes1.next.next.next.next = ListNode(9)
testNodes1.next.next.next.next.next = ListNode(9)
testNodes1.next.next.next.next.next.next = ListNode(9)

testNodes2 = ListNode(9)
testNodes2.next = ListNode(9)
testNodes2.next.next = ListNode(9)
testNodes2.next.next.next = ListNode(9)

print(addTwoNum(testNodes1, testNodes2))