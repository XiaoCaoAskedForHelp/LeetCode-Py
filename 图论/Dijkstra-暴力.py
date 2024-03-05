# 找到起始点到每一个点的最短路径
# 选择一个没有访问过的节点，距离是最小的，然后因为这个点的加入可能会改变最短路径（经过它的路径更短），所以更新
from cmath import inf


def dijkstra(graph, start):
    # 初始化距离表
    distances = {v: inf for v in graph}
    # 设置到起始点的距离为0
    distances[start] = 0
    # 用来存储已经访问过的节点
    visited = []

    for _ in range(len(graph)):
        # 未访问过的节点，选择距离最小的节点
        # 贪心策略：Dijkstra算法是一种贪心算法，它在每一步都寻找最有"希望"（即目前最短距离最小）成为最终最短路径一部分的节点。
        # 这意味着它考虑的是当前已知的全局最小距离，而不仅仅是与已访问节点直接相连的节点。
        # cur = min([v for v in graph if v not in visited], key=lambda v: distances[v])
        # 就算取的不是距离最小的节点也是的，只要把所有节点都能遍历就行
        cur = [v for v in graph if v not in visited][0]
        visited.append(cur)

        # 取到和新添加的这个节点邻接的节点
        for neigh, weight in graph[cur].items():
            # 如果从上一个新添加的节点到邻接节点距离更短，则更新距离表
            new_weight = distances[cur] + weight
            if new_weight < distances[neigh]:
                distances[neigh] = new_weight

    return distances


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

distances = dijkstra(graph, 'A')
print(distances)


def dijkstra1(start):
    n = len(graph1)
    distances = [0] + [inf] * (n - 1)
    visit = [False] * n

    for _ in range(n):
        # 找未访问过，并且距离最小的节点
        cur, dis = 0, inf
        for i in range(n):
            if not visit[i] and distances[i] < dis:
                cur = i
                dis = distances[i]
        visit[cur] = True
        # 与cur相连的点,graph中距离不为inf的坐标
        for j in [index for index, val in enumerate(graph1[cur]) if val != inf]:
            # 新的距离等于从cur到j的距离加上，cur到起点的距离dis
            newdis = graph1[cur][j] + dis
            if newdis < distances[j]:
                distances[j] = newdis

    return distances


graph1 = [
    [0, 1, 4, inf],
    [1, 0, 2, 5],
    [4, 2, 0, 1],
    [inf, 5, 1, 0]
]
distances = dijkstra1(0)
print(distances)
