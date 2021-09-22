class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    class ListNode:
        def __init__(self, value = 0):
            self.data = value
            self.next = None
    
    def __iter__(self):
        curr = self.head
        while curr:
            value = curr.data
            curr = curr.next
            yield value    

    def emptyList(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        if self.head == None and self.tail == None:
            newNode = self.ListNode(value)
            self.head, self.tail = newNode, newNode
        else:
            self.tail.next = self.ListNode(value)
            self.tail = self.tail.next
        self.length += 1
    
    def getNodeBeforeAndAfter(self, value):
        curr = self.head
        index = 0
        while index < value:
            temp = curr
            curr = curr.next
            index += 1
        return temp, curr

    def getValues(self):
        """Return values of all nodes in a list."""
        tempList = []
        while self.head:
            tempList.append(self.head.data)
            self.head = self.head.next
        return tempList

    def getValue(self, index = 0):
        if self.isEmpty() or index >= self.length:
            return None
        elif (self.length - 1) == index:
            return self.tail.data
        else:
            i = 0
            curr = self.head
            while i < index:
                i += 1
                curr = curr.next
            return curr.data

    def isEmpty(self):
        return self.length == 0

    def getLength(self):
        return self.length

    def pop(self, value = None):
        if self.isEmpty():
            return None
        elif self.getLength() == 1: #head and tail are same (length of 1)
            data = self.head.data
            self.head, self.tail = None, None
            self.length -= 1
            return data
        elif value == 0: #pop head
            temp, data = self.head, self.head.data
            self.head = self.head.next
            self.length -= 1
            return data
        if value and value < (self.getLength() - 1): #pop body
            (temp, curr) = self.getNodeBeforeAndAfter(value)
            data, temp.next = curr.data, curr.next
            curr = None
            self.length -= 1
            return data
        else: #pop tail
            (temp,_) = self.getNodeBeforeAndAfter(self.getLength()-1)
            data = temp.next.data
            temp.next = None
            self.tail = temp
            self.length -=1
            return data

ll = LinkedList()
#print(ll.isEmpty())

for item in range(1, 10):
    ll.append(item)
#print(ll.isEmpty())
#ll.pop(2)
#for item in range(1, 10):
#   print(ll.pop(item))
print(ll.isEmpty())
for item in ll:
  print(item)

#print(ll.pop(8))

#anotherList = ll.getValues()

ll.emptyList()

print(ll.isEmpty())
ll.append(1)
ll.append(2)
ll.append(3)

ll.pop(0)
for item in ll:
    print(item)