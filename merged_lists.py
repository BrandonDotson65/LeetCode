# Definition for singly-linked list.
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

    def getVal(self):
        return self.val

    def getValAt(self, index):
        startIndex = 0
        while startIndex < index:
            self = self.next
            startIndex += 1
        return self.val

    def setValAt(self, index, val):
        startIndex = 0
        while startIndex < index:
            self = self.next
            startIndex += 1
        self.val = val
    
    def addNode(self, value):
        while self.next != None:
            self = self.next
        self.next = ListNode(value)

def mergeTwoLists(list1, list2):
    dummy = cur = ListNode(0)
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next

        cur = cur.next
    cur.next = list1 or list2
    return dummy.next


listTemp1 = ListNode(0)
listTemp1.next = ListNode(2)
listTemp1.next.next = ListNode(3)

listTemp2 = ListNode(1)
listTemp2.next = ListNode(1)

mergedList = mergeTwoLists(listTemp1, listTemp2)

#testing iterator

#for values in mergedList:
#    print(values)

#print(mergedList.getValAt(1))
#mergedList.setValAt(0, 2)
#mergedList.addNode(10)
#mergedList.addNode(12)

for values in mergedList:
    print(values)