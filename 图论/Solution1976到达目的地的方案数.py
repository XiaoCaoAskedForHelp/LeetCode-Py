import heapq
from cmath import inf
from collections import deque
from typing import List


class Solution:
    # 下面的写法有问题
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        dp = [[inf, 0] for _ in range(n)]
        g = [[] for _ in range(n)]
        for u, v, time in roads:
            g[u].append([v, time])
            g[v].append([u, time])
        dp[0][0] = 0
        dp[0][1] = 1
        visited = [False for i in range(n)]
        queue = deque([0])
        while queue:
            i = queue.popleft()
            for node, time in g[i]:
                if visited[node]:
                    continue
                if time + dp[i][0] < dp[node][0] and not visited[i]:
                    dp[node][0] = dp[i][0] + time
                    dp[node][1] = dp[i][1]
                    if node != n - 1:
                        queue.append(node)
                elif time + dp[i][0] == dp[node][0] and not visited[i]:
                    dp[node][1] = (dp[node][1] + dp[i][1]) % mod
                    if node != n - 1:
                        queue.append(node)
            visited[i] = True

        return dp[-1][1]

    def countPaths1(self, n: int, roads: List[List[int]]) -> int:
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


Solution().countPaths(7, [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
                          [0, 4, 5], [4, 6, 2]])
