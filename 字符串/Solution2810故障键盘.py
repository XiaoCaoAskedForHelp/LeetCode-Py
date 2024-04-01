from collections import deque


class Solution:
    def finalString(self, s: str) -> str:
        res = []
        for ch in s:
            if ch == "i":
                res.reverse()
            else:
                res.append(ch)
        return "".join(res)


    # 双端队列 O(n) 做法
    # 把反转看成是往字符串的头部添加字符。
    # 如果当前处于「往字符串尾部添加字符」的状态，那么遇到i后，改成「往字符串头部添加字符」的状态。
    # 如果当前处于「往字符串头部添加字符」的状态，那么遇到i后，改成「往字符串尾部添加字符」的状态。
    def finalString1(self, s: str) -> str:
        q = deque()
        tail = True  # 往尾部加是顺序，碰到i翻转后逆序,
        for ch in s:
            if ch == "i":
                tail = not tail
            elif tail:
                q.append(ch)
            else:
                q.appendleft(ch)
        return "".join(q if tail else reversed(q))  # 如果是偶数个i，就不需要翻转



