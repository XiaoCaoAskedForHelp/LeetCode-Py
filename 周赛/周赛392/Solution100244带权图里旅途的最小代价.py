from collections import defaultdict
from typing import List


class Solution:
    # s=t，不移动即可，答案是 000。
    # s 和 t 不在同一个连通块中，答案是 −1。
    # s 和 t 在同一个连通块中。由于 AND 的性质是 AND 的数字越多，结果越小。在可以重复经过边的前提下，最优方案是把 s 所在连通块内的边都走一遍。
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for x, y, c in edges:
            g[x].append((y, c))
            g[y].append((x, c))

        def dfs(x: int):
            and_ = -1
            ids[x] = len(cc_and)  # 记录每个所在连通块的编号
            for y, c in g[x]:
                and_ &= c
                if ids[y] < 0:  # 没有访问过
                    and_ &= dfs(y)
            return and_

        ids = [-1] * n  # 记录每个连通块的编号
        cc_and = []  # 记录每个连通块的边权的and
        for i in range(n):
            if ids[i] < 0:
                cc_and.append(dfs(i))

        return [0 if s == t else -1 if ids[s] != ids[t] else cc_and[ids[s]] for s, t in query]

    # 用并查集的方式去查找连通块
    def minimumCost1(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        fa = [i for i in range(n)]
        and_ = [-1] * n

        def find(x: int):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        for x, y, w in edges:
            x = find(x)
            y = find(y)
            and_[y] &= w
            if x != y:  # 如果x,y的父亲节点不一样，设置x的父亲节点为y
                and_[y] &= and_[x]
                fa[x] = y
        return [0 if s == t else -1 if find(s) != find(t) else and_[find(s)] for s, t in query]


print(Solution().minimumCost(n=10, edges=[[9, 7, 9], [8, 3, 7], [7, 0, 11], [6, 3, 8], [6, 1, 3], [7, 3, 0], [2, 3, 9],
                                          [8, 9, 12]],
                             query=[[0, 6], [1, 0], [2, 9]]))
