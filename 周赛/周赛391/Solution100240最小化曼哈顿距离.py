import heapq
from cmath import inf
from typing import List


class Solution:
    # 超出内存限制
    def minimumDistance(self, points: List[List[int]]) -> int:
        n = len(points)
        queue = []
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dis = abs(x2 - x1) + abs(y2 - y1)
                heapq.heappush(queue, (-dis, (i, j)))
        dis1 = heapq.heappop(queue)
        dis2 = heapq.heappop(queue)
        st1 = set(dis1[1])
        st2 = set(dis2[1])
        point = st1.intersection(st2)
        if not point:
            return abs(dis2[0])
        else:
            res = dis2[0]
            while True:
                dis = heapq.heappop(queue)
                tmp = set(dis[1])
                point = point.intersection(tmp)
                if not point:
                    res = dis[0]
                    break
            return abs(res)

    def minimumDistance1(self, points: List[List[int]]) -> int:
        n = len(points)
        # 使用二维坐标变换为一维坐标计算曼哈顿距离，最长的点就是两边的两点相减，只要是不是去掉这两点，都不会影响最短距离
        vs1 = [(points[i][0] + points[i][1], i) for i in range(n)]
        vs1.sort()
        vs2 = [(points[i][0] - points[i][1], i) for i in range(n)]
        vs2.sort()
        res = inf
        for i in range(n):
            if i == vs1[0][1]:
                v1 = vs1[n - 1][0] - vs1[1][0]
            elif i == vs1[n - 1][1]:
                v1 = vs1[n - 2][0] - vs1[0][0]
            else:
                v1 = vs1[n - 1][0] - vs1[0][0]

            if i == vs2[0][1]:
                v2 = vs2[n - 1][0] - vs2[1][0]
            elif i == vs2[n - 1][1]:
                v2 = vs2[n - 2][0] - vs2[0][0]
            else:
                v2 = vs2[n - 1][0] - vs2[0][0]
            res = min(res, max(v1, v2))
        return res


Solution().minimumDistance(points=[[3, 10], [5, 15], [10, 2], [4, 4]])
