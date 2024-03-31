class Solution:
    # 如果遇到了空节点，则要消耗一个槽位；
    # 如果遇到了非空节点，则除了消耗一个槽位外，还要再补充两个槽位。
    # 用栈来维护槽位的变化。栈中的每个元素，代表了对应节点处剩余槽位的数量，而栈顶元素就对应着下一步可用的槽位数量。
    # 当遇到空节点时，仅将栈顶元素减 1；当遇到非空节点时，将栈顶元素减 1 后，再向栈中压入一个 2。无论何时，如果栈顶元素变为 0，就立刻将栈顶弹出。
    # 遍历结束后，若栈为空，说明没有待填充的槽位，因此是一个合法序列；否则若栈不为空，则序列不合法。此外，在遍历的过程中，若槽位数量不足，则序列不合法。
    def isValidSerialization(self, preorder: str) -> bool:
        n = len(preorder)
        i = 0
        stk = [1]  # 至少需要一个槽位
        while i < n:
            if not stk:
                return False
            if preorder[i] == ",":
                i += 1
            elif preorder[i] == '#':
                stk[-1] -= 1
                if stk[-1] == 0:
                    stk.pop()
                i += 1
            else:
                # 读一个数字
                while i < n and preorder[i] != ",":
                    i += 1
                stk[-1] -= 1
                if stk[-1] == 0:
                    stk.pop()
                stk.append(2)
        return not stk

    def isValidSerialization1(self, preorder: str) -> bool:
        # 回顾方法一的逻辑，如果把栈中元素看成一个整体，即所有剩余槽位的数量，也能维护槽位的变化。
        # 因此，我们可以只维护一个计数器，代表栈中所有元素之和，其余的操作逻辑均可以保持不变。
        n = len(preorder)
        i = 0
        slots = 1
        while i < n:
            if slots == 0:
                return False
            if preorder[i] == ',':
                i += 1
            elif preorder[i] == '#':
                slots -= 1
                i += 1
            else:
                # 读一个数字
                while i < n and preorder[i] != ',':
                    i += 1
                slots += 1  # slots = slots - 1 + 2,因为是数字，所以消耗掉他本身的位置，还需要多加两个槽位
        return slots == 0

    # 牛逼方法，通过一层一层裁剪数字+两个#的最小子树,
    def isValidSerialization2(self, preorder: str) -> bool:
        stack = []
        for node in preorder.split(","):
            stack.append(node)
            while len(stack) >= 3 and stack[-1] == stack[-2] == "#" and stack[
                -3] != "#":  # 将数字+##的子树归并成#好,说明他能形成一个正确的子树
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append("#")
        return len(stack) == 1 and stack.pop() == "#"


Solution().isValidSerialization("1,#,#")
