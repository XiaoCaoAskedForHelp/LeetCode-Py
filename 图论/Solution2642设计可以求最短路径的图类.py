import heapq
from cmath import inf
from typing import List


class Graph:
    # Floyd算法

    # def __init__(self, n: int, edges: List[List[int]]):
    #     self.graph = [[inf] * n for _ in range(n)]
    #     self.n = n
    #     for i in range(n):
    #         self.graph[i][i] = 0
    #     for u, v, c in edges:
    #         self.graph[u][v] = c
    #     for k in range(n):  # 得把k放在外面
    #         for i in range(n):
    #             for j in range(n):
    #                 self.graph[i][j] = min(self.graph[i][k] + self.graph[k][j], self.graph[i][j])
    #
    # def addEdge(self, edge: List[int]) -> None:
    #     u, v, c = edge
    #     if c < self.graph[u][v]:
    #         self.graph[u][v] = c
    #         for i in range(self.n):  # 更新其他的点之间的距离，以edge为桥梁
    #             for j in range(self.n):
    #                 self.graph[i][j] = min(self.graph[i][u] + self.graph[v][j] + c, self.graph[i][j])
    #
    # def shortestPath(self, node1: int, node2: int) -> int:
    #     return self.graph[node1][node2] if self.graph[node1][node2] != inf else -1

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for _ in range(n)]
        for x, y, cost in edges:
            self.graph[x].append((y, cost))

    def addEdge(self, edge: List[int]) -> None:
        x, y, cost = edge
        self.graph[x].append((y, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [inf] * len(self.graph)
        dist[node1] = 0
        q = [(0, node1)]
        while q:
            cost, x = heapq.heappop(q)
            if x == node2:
                return cost
            for y, ncost in self.graph[x]:
                if dist[y] > cost + ncost:
                    dist[y] = cost + ncost
                    heapq.heappush(q, (cost + ncost, y))
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
