from functools import cache
from typing import List


class Solution:
    # dp[i][j] 表示i行和j列的矩形能得到的最大钱数
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for x, y, price in prices:
            dp[x][y] = price
        # 长度和宽度大于1的块都能横着或者竖着被切割分成两块
        for x in range(1, m + 1):  # x和y = 1的时候也需要遍历更新，不然会影响后面的
            for y in range(1, n + 1):
                if x > 1:
                    # 横向分割
                    # for i in range(1, x):
                    for i in range(1, x // 2 + 1): # 分割会出现重复可以优化
                        dp[x][y] = max(dp[i][y] + dp[x - i][y], dp[x][y])
                if y > 1:
                    # 纵向分割
                    # for i in range(1, y):
                    for i in range(1, y // 2 + 1):
                        dp[x][y] = max(dp[x][i] + dp[x][y - i], dp[x][y])
                # 不仅要比分割的两块加起来的大，还要比比他面积小的大
                dp[x][y] = max(dp[x][y], dp[x - 1][y], dp[x][y - 1])
        return dp[-1][-1]

    # 记忆化搜索
    def sellingWood1(self, m: int, n: int, prices: List[List[int]]) -> int:
        value = dict()
        for h, w, price in prices:
            value[(h, w)] = price

        @cache
        def dfs(x: int, y: int):
            ret = value.get((x, y), 0)
            if x > 1:
                for i in range(1, x):
                    ret = max(ret, dfs(i, y) + dfs(x - i, y))
            if y > 0:
                for i in range(1, y):
                    ret = max(ret, dfs(x, i) + dfs(x, y - i))
            return ret

        ans = dfs(m, n)
        dfs.cache_clear()
        return ans


Solution().sellingWood(m=3, n=5, prices=[[1, 4, 2], [2, 2, 7], [2, 1, 3]])
