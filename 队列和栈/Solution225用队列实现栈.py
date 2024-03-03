from collections import deque


class MyStack:

    # def __init__(self):
    #     self.queue = deque()
    #
    # def push(self, x: int) -> None:
    #     self.queue.appendleft(x)
    #
    #
    # def pop(self) -> int:
    #     return self.queue.popleft()
    #
    #
    # def top(self) -> int:
    #     t = self.queue.popleft()
    #     self.queue.appendleft(t)
    #     return t
    #
    # def empty(self) -> bool:
    #     return len(self.queue) == 0

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.queue.popleft())


    def pop(self) -> int:
        return self.queue.popleft()


    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()