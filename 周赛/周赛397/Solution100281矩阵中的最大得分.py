from cmath import inf
from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = -inf
        line = [[-inf] * n for _ in range(m)]
        for i in range(m):
            for j in range(n - 2, -1, -1):
                tmp = max(grid[i][j + 1] - grid[i][j], grid[i][j + 1] - grid[i][j] + line[i][j + 1])
                line[i][j] = tmp
                res = max(tmp, res)

        col = [[-inf] * n for _ in range(m)]
        for j in range(n):
            for i in range(1, m):
                tmp = max(grid[i][j] - grid[i - 1][j], grid[i][j] - grid[i - 1][j] + col[i - 1][j])
                col[i][j] = tmp
                res = max(tmp, res)
        for i in range(m):
            for j in range(n):
                res = max(res, line[i][j] + col[i][j])
        return res


Solution().maxScore(grid=[[4, 3, 2], [3, 2, 1]])
Solution().maxScore(grid=[[9, 5, 7, 3], [8, 9, 6, 1], [6, 7, 14, 3], [2, 5, 3, 1]])
