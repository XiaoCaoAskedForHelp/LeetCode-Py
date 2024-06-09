from functools import cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        # 一段区间的总和是由很多段区间的总和计算出来的
        val = [1] + nums + [1]

        @cache
        def dfs(left: int, right: int):
            # 如果这段区间中间没有数字，那直接返回0
            if left >= right - 1:
                return 0
            best = 0
            for i in range(left + 1, right):
                # 之间这个值加上，两边区间的最大值
                total = val[left] * val[right] * val[i] + dfs(left, i) + dfs(i, right)
                best = max(best, total)
            return best

        return dfs(0, n + 1)

    def maxCoins1(self, nums: List[int]) -> int:
        n = len(nums)
        val = [1] + nums + [1]

        rec = [[0] * (n + 2) for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):  # k 比 i大所以需要从后往前遍历
            for j in range(i + 2, n + 2):  # 区间中至少要由一个数字才能计算
                for k in range(i + 1, j):  # 遍历区间中的每一个值，用与划分区间找出最大值
                    total = val[k] * val[i] * val[j] + rec[i][k] + rec[k][j]
                    rec[i][j] = max(rec[i][j], total)
        return rec[0][n + 1]

