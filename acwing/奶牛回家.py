import heapq
from cmath import inf
from collections import defaultdict

p = int(input())
g = defaultdict(list)
for _ in range(p):
    u, v, c = input().split()
    c = int(c)
    g[u].append((v, c))
    g[v].append((u, c))

# dijkstra算法
distance = defaultdict(int)
queue = [(0, "Z")]
while queue:
    dis, cur = heapq.heappop(queue)
    if distance[cur] != 0 and dis > distance[cur]:
        continue
    for next, c in g[cur]:
        if distance[next] == 0 or (distance[next] != 0 and dis + c < distance[next]):
            distance[next] = dis + c
            heapq.heappush(queue, (distance[next], next))
res = inf
loc = ''
for i in [chr(ord('A') + i) for i in range(25)]:
    if distance[i] != 0 and distance[i] < res:
        res = distance[i]
        loc = i
print(loc, res)
