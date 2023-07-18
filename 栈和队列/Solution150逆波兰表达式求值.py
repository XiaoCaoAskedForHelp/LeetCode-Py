from operator import add, sub, mul


class Solution:
    op_map = {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(x / y)}

    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.op_map[token](op1, op2))
        return stack.pop()

    def evalRPN1(self, tokens: list[str]) -> int:
        stack = []
        for item in tokens:
            if item not in {'+', '-', '*', '/'}:
                stack.append(item)
            else:
                num1, num2 = stack.pop(), stack.pop()
                stack.append(int(eval(f'{num2}{item}{num1}')))
        return int(stack.pop())
