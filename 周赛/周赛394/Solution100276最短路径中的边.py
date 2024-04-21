import heapq
import math
from cmath import inf
from collections import deque
from typing import List


class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        distance = [0] + [inf] * (n - 1)
        queue = [(0, 0)]  # 距离，点

        g = [[] for _ in range(n)]
        for x, y, c in edges:
            g[x].append((y, c))
            g[y].append((x, c))

        edge = set()
        while queue:
            dis, cur = heapq.heappop(queue)
            if dis > distance[cur]:
                continue
            for y, c in g[cur]:
                if dis + c < distance[y]:
                    distance[y] = dis + c
                    heapq.heappush(queue, (distance[y], y))

        # 找到关键路径
        queue = deque([n - 1])
        while queue:
            x = queue.popleft()
            if distance[x] == inf:
                continue
            for y, c in g[x]:
                if distance[x] - c == distance[y]:
                    edge.add((x, y))
                    queue.append(y)
        res = []
        for x, y, v in edges:
            if (x, y) in edge or (y, x) in edge:
                res.append(True)
            else:
                res.append(False)
        return res

    def dijkstra(self, g: List[List[tuple[int]]], start: int) -> List[int]:
        dist = [inf] * len(g)
        dist[start] = 0
        h = [(0, start)]
        while h:
            d, x = heapq.heappop(h)
            if d > dist[x]:
                continue
            for y, wt in g[x]:
                new_d = d + wt
                if new_d < dist[y]:
                    dist[y] = new_d
                    heapq.heappush(h, (new_d, y))
        return dist

    def findAnswer1(self, n: int, edges: List[List[int]]) -> List[bool]:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        dist1 = self.dijkstra(g, 0)
        if dist1[-1] == math.inf:
            return [False] * len(edges)
        dist2 = self.dijkstra(g, n - 1)
        ans = []
        for u, v, w in edges:
            if dist1[u] + dist2[v] + w == dist1[-1] or dist1[v] + dist2[u] + w == dist1[-1]:
                ans.append(True)
            else:
                ans.append(False)
        return ans


Solution().findAnswer1(n=6,
                       edges=[[0, 1, 4], [0, 2, 1], [1, 3, 2], [1, 4, 3], [1, 5, 1], [2, 3, 1], [3, 5, 3], [4, 5, 2]])
