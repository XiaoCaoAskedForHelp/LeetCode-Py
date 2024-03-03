from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]  # (0,0)到(i,j)的面积之和
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dp[i][j] = grid[i][j]
                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]
                # 面积会有重叠需要减去
                if j - 1 >= 0 and i - 1 >= 0:
                    dp[i][j] -= dp[i - 1][j - 1]
                if dp[i][j] <= k:
                    res += 1
        return res


Solution().countSubmatrices([[7, 6, 3], [6, 6, 1]], 18)
