import heapq
from cmath import inf
from collections import defaultdict
from functools import cache


# 不存在减1、减1、在除以2这样的操作，(m-1-1)/2 = m /2 -1  完全可以变为除以2在减1，少一次操作
# 不存在减1、减1、减1在除以3这样的操作，证明和上面同理

class Solution:
    # 多做除法比多做减法好
    # dfs(i)把i变为0的最小操作次数
    # dfs(i) = min(dfs(⌊i / 2⌋)+imod2, dfs(⌊i / 3⌋)+imod3)+1
    def minDays(self, n: int) -> int:
        @cache
        def dfs(i: int):
            if i <= 1:
                return i
            return min(dfs(i // 2) + i % 2, dfs(i // 3) + i % 3) + 1

        return dfs(n)

    # x 到 ⌊x/2⌋ 连一条边权为x mod 2 + 1的边
    # x 到 ⌊x/3⌋ 连一条边权为x mod 3 + 1的边
    # 1 到 0 连一条边权为1 的边
    # 求n到0的最短路，Dijkstra算法
    def minDays1(self, n: int) -> int:
        dis = defaultdict(lambda: inf)
        h = [(0, n)]
        while h:
            dx, x = heapq.heappop(h)
            if x <= 1:
                return dx + x
            if dx > dis[x]:
                continue
            for d in 2, 3:
                y = x // d  # 算出能到的节点
                dy = dx + x % d + 1  # 加上边权，算出此时的最小操作次数，1就是选2或选3走的那一步，x%d就是需要变为能整除2或3所需走的步数
                if dy < dis[y]:
                    dis[y] = dy
                    heapq.heappush(h, (dy, y))  # 将操作次数更优的放入队列中
