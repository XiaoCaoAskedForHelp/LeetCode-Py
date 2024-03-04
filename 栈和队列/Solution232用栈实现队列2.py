class MyQueue:

    # def __init__(self):
    #     self.data = []  # 数据栈
    #     self.stack = []  # 辅助栈
    #
    # def push(self, x: int) -> None:
    #     # 因为栈是先进后出的，但是队列是先进先出的，栈顶相当于队头，需要把新加入的放到队尾也就是栈底
    #     # 先把数据从数据栈转移出去
    #     while self.data:
    #         self.stack.append(self.data.pop())
    #     # 把新数据放在栈底，也就是队尾
    #     self.data.append(x)
    #     while self.stack:
    #         self.data.append(self.stack.pop())
    #
    # def pop(self) -> int:
    #     return self.data.pop()
    #
    # def peek(self) -> int:
    #     return self.data[-1]
    #
    # def empty(self) -> bool:
    #     return not self.data


    def __init__(self):
        self.stack_in = [] # 负责push
        self.stack_out = [] # 负责pop

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.stack_out:
            return self.stack_out.pop()
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()


    def peek(self) -> int:
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)
