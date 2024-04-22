from functools import cache
from typing import List


class Solution:
    # 完全背包排序问题
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for j in nums:
                if i - j >= 0:
                    dp[i] += dp[i - j]
        return dp[-1]

    # 递归，记忆化搜索
    def combinationSum41(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i: int):
            if i == 0:
                return 1
            return sum(dfs(i - x) for x in nums if x <= i)

        return dfs(target)

    def combinationSum42(self, nums: List[int], target: int) -> int:
        f = [1] + [0] * target
        for i in range(1, target + 1):
            f[i] = sum(f[i - x] for x in nums if x <= i)
        return f[target]
