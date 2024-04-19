import math
from functools import cache
from itertools import count
from typing import List


class Solution:
    # 如果最多跳 2 次，用「选或不选」分类讨论
    # 在最多跳过 i 次的情况下，从 dist[0] 到 dist[j] 需要的最小时间」，所以把它定义成 dfs(i,j)
    # 为了避免浮点运算，把 dfs(i,j)的定义改成在同等时间下用 speed 速度能走的距离
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        if sum(dist) > hoursBefore * speed:
            return -1

        @cache
        def dfs(i: int, j: int):
            if j < 0:
                return 0
            res = (dfs(i, j - 1) + dist[
                j] + speed - 1) // speed * speed  # 不跳过j,用时(dfs(i, j - 1) + dist[j])/speed 上取整在成speed
            if i:
                res = min(res, dfs(i - 1, j - 1) + dist[j])  # 跳过j,消耗掉一次i，那就是之前的dfs(i-1,j-1) + dist[j]
            return res

        for i in count(0):
            if dfs(i, len(dist) - 2) + dist[-1] <= speed * hoursBefore:
                return i

    # f[i][j] 的定义和 dfs(i,j) 的定义是一样的，都表示在最多跳过 i 次的情况下，从 dist[0] 到 dist[j] 需要的最小时间，再乘上 speed
    def minSkips1(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        if sum(dist) > speed * hoursBefore:
            return -1
        n = len(dist)
        f = [[0] * n for _ in range(n)]
        for i in count(0):
            for j, d in enumerate(dist[:-1]):
                f[i][j + 1] = (f[i][j] + d + speed - 1) // speed * speed
                if i:
                    f[i][j + 1] = min(f[i][j + 1], f[i - 1][j] + d)
            if f[i][-1] + dist[-1] <= speed * hoursBefore:
                return i

    # 空间优化
    def minSkips2(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        if sum(dist) > speed * hoursBefore:
            return -1
        f = [0] * len(dist)
        for i in count(0):
            pre = 0
            for j, d in enumerate(dist[:-1]):
                tmp = f[j + 1]
                f[j + 1] = (f[j] + d + speed - 1) // speed * speed
                if i:
                    f[j + 1] = min(f[j + 1], pre + d)
                pre = tmp
            if f[-1] + dist[-1] <= speed * hoursBefore:
                return i

Solution().minSkips(dist=[1, 3, 2], speed=4, hoursBefore=2)
