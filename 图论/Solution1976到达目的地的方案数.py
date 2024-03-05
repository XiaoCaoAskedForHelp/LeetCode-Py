import heapq
from cmath import inf
from typing import List


class Solution:
    # dijkstra算法
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        e = [[] for _ in range(n)]
        for x, y, t in roads:
            e[x].append([y, t])
            e[y].append([x, t])
        times = [0] + [inf] * (n - 1)
        ways = [1] + [0] * (n - 1)

        queue = [[0, 0]]  # 路径长度和点的编号
        while queue:
            t, u = heapq.heappop(queue)
            if t > times[u]:
                continue
            for v, w in e[u]:
                if w + times[u] < times[v]:
                    times[v] = w + times[u]
                    ways[v] = ways[u]
                    heapq.heappush(queue, (times[v], v))
                elif w + times[u] == times[v]:
                    ways[v] = (ways[v] + ways[u]) % mod
        return ways[-1]

    def countPaths1(self, n: int, roads: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        e = [[] for _ in range(n)]
        for x, y, t in roads:
            e[x].append([y, t])
            e[y].append([x, t])
        times = [0] + [inf] * (n - 1)
        ways = [1] + [0] * (n - 1)
        visited = [False] * n

        queue = [[0, 0]]  # 路径长度和点的编号
        while queue:
            t, u = heapq.heappop(queue)
            if visited[u]:
                continue  # 只要能用上所有的点就行
            visited[u] = True
            for v, w in e[u]:
                if w + times[u] < times[v]:
                    times[v] = w + times[u]
                    ways[v] = ways[u]
                    heapq.heappush(queue, (times[v], v))
                elif w + times[u] == times[v]:
                    ways[v] = (ways[v] + ways[u]) % mod
        return ways[-1]

    def countPaths2(self, n: int, roads: List[List[int]]) -> int:
        matrix = [[inf] * n for _ in range(n)]
        cnt = [[0] * n for _ in range(n)]
        for i in range(n):
            matrix[i][i] = 0
            cnt[i][i] = 1
        for road in roads:
            matrix[road[0]][road[1]] = road[2]
            matrix[road[1]][road[0]] = road[2]
            cnt[road[0]][road[1]] = 1
            cnt[road[1]][road[0]] = 1
        mod = 10 ** 9 + 7
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if k != i and k != j:
                        sum = matrix[i][k] + matrix[k][j]
                        if matrix[i][j] == sum:
                            cnt[i][j] = (cnt[i][k] * cnt[k][j] + cnt[i][j]) % mod
                        elif sum < matrix[i][j]:
                            matrix[i][j] = sum
                            cnt[i][j] = (cnt[i][k] * cnt[k][j]) % mod

        return cnt[0][n - 1]


Solution().countPaths(7, [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
                          [0, 4, 5], [4, 6, 2]])
