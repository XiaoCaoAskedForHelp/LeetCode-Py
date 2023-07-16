class MyQueue:

    def __init__(self):
        self.stackin = []
        self.stackout = []

    def push(self, x: int) -> None:
        self.stackin.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        if self.stackout:
            return self.stackout.pop()
        else:
            for i in range(len(self.stackin)):
                self.stackout.append(self.stackin.pop())
            return self.stackout.pop()

    def peek(self) -> int:
        ans = self.pop()
        self.stackout.append(ans)
        return ans

    def empty(self) -> bool:
        return not (self.stackin or self.stackout)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
