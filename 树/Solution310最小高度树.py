import copy
from cmath import inf
from collections import deque
from typing import List


class Solution:
    # 求出路径最长的两个叶子节点即可，并求出其路径的最中间的节点即为最小高度树的根节点
    # 图中距离最远的两个节点和他们之间的路径：
    # 1. 与任意节点p出发，利用dfs或bfs找到以p为起点的最长路径的终点x，p就是根节点
    # 2. 与x出发，找到以x为起点的最长路径的终点y
    # 3. x到y之间的路径即为图中的最长路径，找到路径中间节点即为根节点

    # 广度优先搜索
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0] * n

        def bfs(start: int):
            visited = [False] * n
            visited[start] = True
            q = deque([start])
            x = start
            while q:
                x = q.popleft()
                for y in g[x]:
                    if not visited[y]:
                        q.append(y)
                        visited[y] = True
                        parents[y] = x
            return x

        x = bfs(0)  # 找到与节点 0 最远的节点 x
        y = bfs(x)  # 找到与节点 x 最远的节点 y

        path = []
        # 通过不断的找父亲节点，形成路径
        parents[x] = -1
        while y != -1:
            path.append(y)
            y = parents[y]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2 - 1], path[m // 2]]

    def findMinHeightTrees1(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        parents = [0] * n

        maxDepth, node = 0, 0

        def dfs(x: int, pa: int, depth: int):
            nonlocal maxDepth, node
            if depth > maxDepth:
                maxDepth, node = depth, x
            parents[x] = pa
            for i in g[x]:
                if i != pa:
                    dfs(i, x, depth + 1)

        dfs(0, -1, 1)
        maxDepth = 0
        dfs(node, -1, 1)

        path = []
        while node != -1:
            path.append(node)
            node = parents[node]
        m = len(path)
        return [path[m // 2]] if m % 2 else [path[m // 2], path[m // 2 - 1]]

    # 拓扑排序，反复删除最外层度为 1 的节点直到剩下根节点为止
    def findMinHeightTrees2(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        g = [[] for _ in range(n)]
        deg = [0] * n
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            deg[x] += 1
            deg[y] += 1

        q = [i for i, d in enumerate(deg) if d == 1]
        remain = n
        while remain > 2:  # 剩一个或者两个节点的时候一定是跟
            remain -= len(q)
            tmp = q
            q = []
            for x in tmp:
                for y in g[x]:
                    deg[y] -= 1
                    if deg[y] == 1:
                        q.append(y)
        return q


Solution().findMinHeightTrees(n=6, edges=[[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]])
Solution().findMinHeightTrees(n=6, edges=[[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]])
Solution().findMinHeightTrees(n=4, edges=[[1, 0], [1, 2], [1, 3]])
