from cmath import inf
from typing import List


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        n = len(possible)
        for i in range(n):
            if possible[i] == 0:
                possible[i] = -1
        # 计算前缀和后缀表达式,前缀表达式代表完成前i关得分
        pre = [0] * (n + 1)
        for i in range(1, n):
            pre[i] = pre[i - 1] + possible[i - 1]
        last = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            last[i] = last[i + 1] + possible[i]
        for i in range(1, n):
            if pre[i] > last[i]:
                return i
        return -1


print(Solution().minimumLevels(possible=[1, 0, 1, 0]))
