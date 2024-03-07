from cmath import inf
from functools import cache
from typing import List


class Solution:
    # dp
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[inf] * n for _ in range(m)]
        for i in range(n):
            dp[0][i] = grid[0][i]
        for i in range(1, m):
            for j in range(n):
                for prej in range(n):
                    cost = moveCost[grid[i - 1][prej]][j]
                    dp[i][j] = min(dp[i][j], dp[i - 1][prej] + grid[i][j] + cost)
        return int(min(dp[-1]))

    # dp
    def minPathCost1(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[inf] * n for _ in range(2)]
        for i in range(n):
            dp[0][i] = grid[0][i]
        for i in range(1, m):
            for j in range(n):
                for prej in range(n):
                    cost = moveCost[grid[i - 1][prej]][j]
                    dp[i % 2][j] = min(dp[i % 2][j], dp[(i - 1) % 2][prej] + grid[i][j] + cost)
            # 需要将上一次记录的值变为inf，不然无法更新了
            for j in range(n):
                dp[(i - 1) % 2][j] = inf
        return int(min(dp[(m - 1) % 2]))

    def minPathCost2(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = grid[0]
        for i in range(1, m):
            # 直接创建好新的数组然后一起填回去，不能一个一个填回去，会出现覆盖问题
            dp = [grid[i][j] + min(dp[k] + moveCost[grid[i - 1][k]][j] for k in range(n)) for j in range(n)]

        return min(dp)

    # 记忆化搜索
    def minPathCost3(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        @cache
        def dfs(i: int, j: int):
            if i == 0:
                return grid[i][j]
            return min(dfs(i - 1, k) + grid[i][j] + moveCost[grid[i - 1][k]][j] for k in range(len(grid[0])))

        return min(dfs(len(grid) - 1, j) for j in range(len(grid[0])))

    def minPathCost4(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[-1] * n for _ in range(m)]

        def dfs(i: int, j: int):
            if i == 0:
                return grid[i][j]
            if memo[i][j] > 0:
                return memo[i][j]
            memo[i][j] = min(dfs(i - 1, k) + grid[i][j] + moveCost[grid[i - 1][k]][j] for k in range(len(grid[0])))
            return memo[i][j]

        return min(dfs(len(grid) - 1, j) for j in range(len(grid[0])))


Solution().minPathCost1(grid=[[5, 3], [4, 0], [2, 1]], moveCost=[[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]])
