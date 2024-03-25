from functools import cache
from typing import List

import cachetools


class Solution:
    # 组合数，所以先遍历物品，这样顺序固定不会出现{1,2}和{2,1}这样的重复解
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        # 遍历物品
        for i in range(len(coins)):
            # 遍历背包
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
        return dp[amount]

    # dfs(i,c) 表示用前 i 种硬币组成金额 c 的方案数，考虑「选或不选」
    def change1(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i: int, c: int):
            if i < 0:
                return 1 if c == 0 else 0
            if c < coins[i]:
                return dfs(i - 1, c)  # 如果当前的硬币大于金额，那么只能使用前面更小的硬盘去组合
            return dfs(i - 1, c) + dfs(i, c - coins[i])  # 不在选用第i种硬币和继续选一枚第i种硬币

        return dfs(len(coins) - 1, amount)
