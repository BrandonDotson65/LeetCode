#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        string = ""
        while self:
            string += str(self.val) + " "
            self = self.next
        return string
    def __iter__(self):
        while self:
            val = self.val
            self = self.next
            yield val
    def printNodes(self):
        tempList = []
        while self:
            tempList.append(self.val)
            self = self.next
        return tempList

    def addNode(self, value):
        while self.next != None:
            self = self.next
        self.next = ListNode(value)

def deleteDuplicates(headNode):
    curr, prev = headNode, None
    while curr:
        if (prev and prev.val == curr.val):
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next
    return headNode


testNodes = ListNode(1)

testNodes.addNode(1)
testNodes.addNode(2)
testNodes.addNode(3)
testNodes.addNode(3)

print(deleteDuplicates(testNodes))