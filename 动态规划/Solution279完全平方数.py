class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):  # 遍历背包
            for j in range(1, int(i ** 0.5) + 1):  # 遍历物品
                # 更新凑成数字 i 所需的最少完全平方数数量
                dp[i] = min(dp[i], dp[i - j * j] + 1)

        return dp[n]

    def numSquares1(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, int(n ** 0.5) + 1):  # 遍历物品
            for j in range(i * i, n + 1):  # 遍历背包
                # 更新凑成数字 j 所需的最少完全平方数数量
                dp[j] = min(dp[j - i * i] + 1, dp[j])

        return dp[n]
