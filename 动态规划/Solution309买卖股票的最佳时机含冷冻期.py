from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        dp = [[0] * 4 for _ in range(n)]
        dp[0][0] = -prices[0]  # 初始状态：第一天持有股票的最大利润为买入股票的价格
        for i in range(1, n):
            # 达到买入股票状态
            dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][3], dp[i - 1][1]) - prices[i])
            # 达到保持卖出股票状态
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
            # 达到今天就卖出股票状态
            dp[i][2] = dp[i - 1][0] + prices[i]
            # 达到冷冻期状态
            dp[i][3] = dp[i - 1][2]
        return max(dp[n - 1][3], dp[n - 1][1], dp[n - 1][2])  # 返回最后一天不持有股票的最大利润
