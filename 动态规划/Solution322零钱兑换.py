from cmath import inf
from functools import cache
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)  # 创建动态规划数组，初始值为正无穷大
        dp[0] = 0  # 初始化背包容量为0时的最小硬币数量为0

        for coin in coins:  # 遍历硬币列表，相当于遍历物品
            for i in range(coin, amount + 1):  # 遍历背包容量
                # 这一行可以去掉，因为float('inf') + 1还是inf，不会向其他语言一样变为负数，但是会多做很多无用的比较
                if dp[i - coin] != float('inf'):  # 如果dp[i - coin]不是初始值，则进行状态转移
                    dp[i] = min(dp[i - coin] + 1, dp[i])  # 更新最小硬币数量

        if dp[amount] == float('inf'):  # 如果最终背包容量的最小硬币数量仍为正无穷大，表示无解
            return -1
        return dp[amount]  # 返回背包容量为amount时的最小硬币数量

    # 先遍历物品后遍历背包（优化版）
    def coinChange1(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):  # 进行优化，从能装得下的背包开始计算，则不需要进行比较
                # 更新凑成金额 i 所需的最少硬币数量
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

    # 先遍历背包 后遍历物品（优化版）
    def coinChange2(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):  # 遍历背包容量
            for coin in coins:  # 遍历物品
                if i - coin >= 0:
                    # 更新凑成金额 i 所需的最少硬币数量
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange3(self, coins: List[int], amount: int) -> int:
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