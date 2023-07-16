from collections import deque


class MyStack:

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        n = len(self.que)
        self.que.append(x)
        for i in range(n):
            self.que.append(self.que.popleft())

    def pop(self) -> int:
        return self.que.popleft()


    def top(self) -> int:
        return self.que[0]


    def empty(self) -> bool:
        return not self.que


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()