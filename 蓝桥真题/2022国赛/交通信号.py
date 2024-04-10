import collections
import heapq
import math

n, m, s, t = map(int, input().split())
graph = collections.defaultdict(list)
for i in range(m):
    u, v, g, r, d = map(int, input().split())
    graph[u].append([v, g, r, d, 0])
    graph[v].append([u, r, g, d, 1])  # 对v到u来说红灯的市场就是绿灯的时长
# 结点和其到起始结点的距离
dist = [math.inf] * (n + 1)
dist[s] = 0
heap = [(0, s)]
# 使用dijkstra算法找出最短路径
while heap:
    dis, u = heapq.heappop(heap)
    if dist[u] < dis:
        continue
    for v, g, r, d, f in graph[u]:  # 遍历跟u相连的所有v
        cycle = g + r + d + d  # 信号灯的循环周期
        if not f:  # 如果是绿灯通行正向行驶,正好碰到绿灯不需要等待
            wait = cycle - dis % cycle if dis % cycle >= g else 0
        else:
            if dis >= r + d:
                wait = (cycle - (dis - r - d) % cycle) % cycle if (dis - r - d) % cycle >= g else 0
            else:  # dis < r + d 只要能熬过绿灯时间，就能正常通行
                wait = r + d - dis

        # 如果经过当前节点到邻居节点的路径
        if dis + wait + d < dist[v]:
            dist[v] = dis + wait + d
            heapq.heappush(heap, (dist[v], v))
# 如果目标节点的距离仍为无穷大，说明没有路径，输出1，否则输出距离
print(dist[t] if dist[t] < math.inf else -1)
