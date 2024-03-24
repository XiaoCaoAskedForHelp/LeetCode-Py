from cmath import inf
from functools import cache
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        # 遍历物品
        for i in range(len(coins)):
            # 遍历背包
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
        return dp[amount]

    def coinChange1(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                # if i - coin >= 0 and (i - coin == 0 or dp[i - coin] != 0):
                if i - coin >= 0:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        return -1 if dp[-1] == inf else dp[-1]

    def coinChange2(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(amo: int):
            if amo < 0:
                return -1
            if amo == 0:
                return 0
            mini = inf
            for coin in coins:
                res = dfs(amo - coin)
                if res >= 0 and res < mini:
                    mini = res + 1
            return mini if mini < inf else -1

        return dfs(amount)


Solution().coinChange1(coins=[1, 2, 5], amount=11)
