from functools import cache
from math import comb


class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def dfs(step: int, jump: int, flag: bool):
            if step < 0:
                return 0
            if jump > 30:
                return 0
            cnt = 0
            if step == k:
                cnt += 1
            if not flag:
                cnt += dfs(step - 1, jump, True)
            cnt += dfs(step + 2 ** jump, jump + 1, False)
            return cnt

        return dfs(1, 0, False)

    def waysToReachStair1(self, k: int) -> int:
        @cache
        def dfs(i: int, j: int, pre_down: bool):
            if i > k + 1:  # 由于操作1不能连续使用，无法到达k
                return 0
            res = 1 if i == k else 0
            res += dfs(i + (1 << j), j + 1, False)  # 操作2
            if i and not pre_down:
                res += dfs(i - 1, j, True)  # 操作1
            return res

        return dfs(1, 0, False)

    def waysToReachStair1(self, k: int) -> int:
        ans = 0
        for j in range(30):
            m = (1 << j) - k  # 操作1的次数
            if 0 <= m <= j + 1:
                ans += comb(j + 1, m)  # comb是用来计算组合数的
        return ans


print(Solution().waysToReachStair(0))
print(Solution().waysToReachStair(1))
