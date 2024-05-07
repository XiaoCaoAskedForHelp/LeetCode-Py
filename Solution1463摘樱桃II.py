import heapq
from functools import cache
from typing import List


class Solution:
    # dfs(i,j,k) 递归
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int, k: int):
            if j < 0 or j >= n or k < 0 or k >= n:
                return 0
            if i == m - 1:
                return grid[-1][j] + (grid[-1][k] if j != k else 0)
            return max(dfs(i + 1, j - 1, k - 1), dfs(i + 1, j - 1, k), dfs(i + 1, j - 1, k + 1),
                       dfs(i + 1, j, k - 1), dfs(i + 1, j, k), dfs(i + 1, j, k + 1),
                       dfs(i + 1, j + 1, k - 1), dfs(i + 1, j + 1, k), dfs(i + 1, j + 1, k + 1)) + grid[i][j] + (
                grid[i][k] if j != k else 0)
            # return max(dfs(i + 1, j2, k2) for j2 in (j - 1, j, j + 1) for k2 in (k - 1, k, k + 1)) + grid[i][j] + (
            #     grid[i][k] if j != k else 0)

        return dfs(0, 0, n - 1)

    # f[i][j][k] 的定义和 dfs(i,j,k) 的定义是一样的，都表示 A 从 (i,j) 出发，B 从 (i,k) 出发，到达最后一行，可以得到的樱桃个数的最大值。

    def cherryPickup1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[[0] * (n + 2) for _ in range(n + 2)] for _ in range(m + 1)]  # n + 2 是因为要同时考虑两边的边界情况
        for i in range(m - 1, -1, -1):  # 从下往上遍历，这样答案就显而易见
            for j in range(min(i + 1, n)):  # 一直向右下角走，最多也就是(i,i)
                for k in range(max(j + 1, n - 1 - i), n):  # 一直朝左下角走，最多也就是(i,n-1-i)
                    f[i][j + 1][k + 1] = max(
                        f[i + 1][j][k], f[i + 1][j][k + 1], f[i + 1][j][k + 2],
                        f[i + 1][j + 1][k], f[i + 1][j + 1][k + 1], f[i + 1][j + 1][k + 2],
                        f[i + 1][j + 2][k], f[i + 1][j + 2][k + 1], f[i + 1][j + 2][k + 2],
                    ) + grid[i][j] + grid[i][k]  # j和k的范围保证了两者不会出现重叠的情况
        return f[0][1][n]  # 结果就是位于(0,0)和(0，n-1)的情况

    def cherryPickup2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pre = [[0] * (n + 2) for _ in range(n + 2)]
        cur = [[0] * (n + 2) for _ in range(n + 2)]
        for i in range(m - 1, -1, -1):
            for j in range(min(i + 1, n)):
                for k in range(max(j + 1, n - 1 - i), n):
                    cur[j + 1][k + 1] = max(
                        pre[j][k], pre[j][k + 1], pre[j][k + 2],
                        pre[j + 1][k], pre[j + 1][k + 1], pre[j + 1][k + 2],
                        pre[j + 2][k], pre[j + 2][k + 1], pre[j + 2][k + 2],
                    ) + grid[i][j] + grid[i][k]
            pre, cur = cur, pre  # 下一个i的pre是cur
        return pre[1][n]


Solution().cherryPickup1([[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]])
