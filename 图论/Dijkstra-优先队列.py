import heapq
from cmath import inf


# 优先队列，维持一个最小堆
def dijkstra(graph, start):
    # 初始化距离表
    distances = {v: inf for v in graph}
    # 将起点距离设为0
    distances[start] = 0
    # 用来存储(距离，节点)对的优先队列 ,默认按照元组中的第一个元素进行排序
    queue = [(0, start)]
    while queue:
        # 去除队列中的最小的节点
        distance, cur = heapq.heappop(queue)

        # 如果刚节点的距离已经被其他节点更新过了，当最小堆的底部距离长的节点来更新时就会出现，它比这个节点到起点的距离都长，那肯定直接跳过了
        if distance > distances[cur]:
            continue

        # 遍历所有的邻接节点
        for neigh, weigh in graph[cur].items():
            new_weight = weigh + distance
            if new_weight < distances[neigh]:
                distances[neigh] = new_weight
                # 如果找到更短的路径，则更新优先队列，因为可能别的节点可以通过这个节点，将路径减少
                heapq.heappush(queue, (new_weight, neigh))
    return distances


# 示例图
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 计算从起点A到所有节点的最短路径
distances = dijkstra(graph, 'A')
print(distances)

# 使用了一个visited布尔数组来标记每个节点是否已经被访问（即，其最短路径已经被找到）。
# 一旦一个节点被从优先队列中取出，它就被标记为已访问，其最短路径被认为是确定的，
# 因此该节点在后续的迭代中会被忽略。
def dijkstra1(start):
    n = len(graph1)
    distances = [0] + [inf] * (n - 1)
    visited = [False] * n
    queue = [(0, start)]
    while queue:
        distance, cur = heapq.heappop(queue)
        if visited[cur]:
            continue
        visited[cur] = True
        for i in range(n):
            if graph1[cur][i] == inf:
                continue
            if graph1[cur][i] + distance < distances[i]:
                distances[i] = graph1[cur][i] + distance
                heapq.heappush(queue, (distances[i], i))

    return distances
# 依靠检查当前从优先队列中取出的节点的距离与distances数组中存储的该节点的最短距离。
# 如果队列中的距离大于distances数组中的距离，这意味着该节点的更短路径已经被找到，
# 当前取出的路径可以被忽略。
# 这样比较省存储空间
def dijkstra2(start):
    n = len(graph1)
    distances = [0] + [inf] * (n - 1)
    queue = [(0, start)]
    while queue:
        distance, cur = heapq.heappop(queue)
        if distance > distances[cur]:
            continue
        for i in range(n):
            if graph1[cur][i] == inf:
                continue
            if graph1[cur][i] + distance < distances[i]:
                distances[i] = graph1[cur][i] + distance
                heapq.heappush(queue, (distances[i], i))

    return distances


graph1 = [
    [0, 1, 4, inf],
    [1, 0, 2, 5],
    [4, 2, 0, 1],
    [inf, 5, 1, 0]
]
distances = dijkstra1(0)
print(distances)
distances = dijkstra2(0)
print(distances)
