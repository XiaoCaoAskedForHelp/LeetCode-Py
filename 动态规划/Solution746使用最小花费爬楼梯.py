from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        dp[0] = 0  # 初始值，表示从起点开始不需要花费体力
        dp[1] = 0  # 初始值，表示经过第一步不需要花费体力

        for i in range(2, len(cost) + 1):
            # 在第i步，可以选择从前一步（i-1）花费体力到达当前步，或者从前两步（i-2）花费体力到达当前步
            # 选择其中花费体力较小的路径，加上当前步的花费，更新dp数组
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[-1]  # 返回到达楼顶的最小花费

    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        dp0 = 0  # 初始值，表示从起点开始不需要花费体力
        dp1 = 0  # 初始值，表示经过第一步不需要花费体力

        for i in range(2, len(cost) + 1):
            # 在第i步，可以选择从前一步（i-1）花费体力到达当前步，或者从前两步（i-2）花费体力到达当前步
            # 选择其中花费体力较小的路径，加上当前步的花费，得到当前步的最小花费
            dpi = min(dp1 + cost[i - 1], dp0 + cost[i - 2])

            dp0 = dp1  # 更新dp0为前一步的值，即上一次循环中的dp1
            dp1 = dpi  # 更新dp1为当前步的最小花费

        return dp1  # 返回到达楼顶的最小花费

    # 假设题意为到达第一步和第二步就需要花费
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        n = len(cost)
        prev_1 = cost[0]  # 前一步的最小花费
        prev_2 = cost[1]  # 前两步的最小花费
        for i in range(2, n):
            current = min(prev_1, prev_2) + cost[i]  # 当前位置的最小花费
            prev_1, prev_2 = prev_2, current  # 更新前一步和前两步的最小花费
        return min(prev_1, prev_2)  # 最后一步可以理解为不用花费，取倒数第一步和第二步的最少值