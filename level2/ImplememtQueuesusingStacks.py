class MyQueue:

    def __init__(self):
        self.s = collections.deque()
        
    def push(self, x: int) -> None:
        self.s.append(x)
        for x in range(len(self.s)-1):
            self.s.append(self.s.popleft())
        
    def pop(self) -> int:
         return self.s.pop()
        

    def peek(self) -> int:
        return self.s[-1]

    def empty(self) -> bool:
        return not len(self.s)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
