# 依次将每个点作为中间点去做更新
from cmath import inf


def floyd(graph):
    n = len(graph)
    # distance数组，distance[i][j]是从i到j的最短距离
    # 初始情况下，distance数组的值等于图的邻接矩阵的值
    distances = list(map(lambda i: list(map(lambda j: j, i)), graph))

    # 对每个节点k，更新所有节点对(i, j)的最短距离
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # k != i && k != j 可以判断一下
                # 如果通过节点k的路径比直接从i到j的路径更短，则更新distance[i][j]
                distances[i][j] = min(distances[i][k] + distances[k][j], distances[i][j])

    return distances


graph = [
    [0, 5, inf, 10],
    [inf, 0, 3, inf],
    [inf, inf, 0, 1],
    [inf, inf, inf, 0]
]
distances = floyd(graph)

for row in distances:
    print(row)
