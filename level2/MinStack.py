class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        self.items.insert(0, val)

    def pop(self) -> None:
        self.items.pop(0)

    def top(self) -> int:
        return self.items[0]

    def getMin(self) -> int:
        return min(self.items)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
