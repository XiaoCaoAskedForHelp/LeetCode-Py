import math

n, d = map(int, input().split())

dis = [[0] * n for _ in range(n)]
points = []
for i in range(n):
    points.append([int(i) for i in input().split()])

for i in range(n):
    for j in range(n):
        if i != j:
            x1, y1 = points[i]
            x2, y2 = points[j]
            dis[i][j] = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)



print()
