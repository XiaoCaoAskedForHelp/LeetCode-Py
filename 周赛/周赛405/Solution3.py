from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[(0, 0) for j in range(n + 1)] for i in range(m + 1)]
        res = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j][0] = dp[i - 1][j][0] + dp[i][j - 1][0] - dp[i - 1][j - 1][0] + (
                    1 if grid[i - 1][j - 1] == 'X' else 0)
                dp[i][j][1] = dp[i - 1][j][1] + dp[i][j - 1][1] - dp[i - 1][j - 1][1] + (
                    1 if grid[i - 1][j - 1] == 'Y' else 0)
                if dp[i][j][0] == dp[i][j][1] and dp[i][j][0] != 0:
                    res += 1
        return res


Solution().numberOfSubmatrices([["X", "Y", "."], ["Y", ".", "."]])
