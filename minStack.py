class MinStack:

    def __init__(self):
        self.stack = []
        """
        initialize your data structure here.
        """
    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append(min(self.stack[-2], val))
        else:
            self.stack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.stack.pop()
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[-2]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

stack = MinStack()

stack.push(1)
stack.push(3)
stack.push(9)

print(stack.getMin())