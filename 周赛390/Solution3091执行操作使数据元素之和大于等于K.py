from cmath import inf
from functools import cache


class Solution:
    # 操作最大的元素就行
    # 超出内存限制
    def minOperations(self, k: int) -> int:
        @cache
        def dfs(k: int, m: int, s: int, op: int):
            if s >= k:
                return op
            return min(dfs(k, m + 1, s + 1, op + 1), dfs(k, m, s + m, op + 1))

        return dfs(k, m=1, s=1, op=0)  # m为nums中最大的数字,s为nums之和,op表示最小的操作次数

    # 肯定是先做+1操作，在进行翻倍    贪心
    # 所以我任务可以直接枚举+1的次数
    def minOperations1(self, k: int) -> int:
        res = inf
        for i in range(0, k // 2 + 1):
            num = 1 + i
            copynum = (k // num + 1 if k % num else k // num) - 1
            res = min(res, i + copynum)  # i就是+1的操作次数，后面就是复制的操作次数
        return res

    def minOperations2(self, k: int) -> int:
        ans = k - 1
        for i in range(k):
            c = (k - 1) // (i + 1)
            ans = min(ans, c + i)
        return ans
