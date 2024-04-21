from cmath import inf
from collections import Counter, defaultdict
from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dic = []
        for j in range(n):
            tmp = defaultdict(int)
            for i in range(m):
                tmp[grid[i][j]] += 1
            dic.append(tmp)
        dp = [[inf] * 10 for _ in range(n)]
        for j in range(n):
            tmp = dic[j]
            # for k, v in tmp.items():
            for k in range(10):
                v = tmp[k] if tmp.get(k) else 0
                if j == 0:
                    dp[j][k] = m - v
                else:
                    dp[j][k] = min(dp[j - 1][num] for num in range(10) if num != k) + m - v

        return min(dp[-1])


Solution().minimumOperations(grid = [[1,0,2],[1,0,2]])
