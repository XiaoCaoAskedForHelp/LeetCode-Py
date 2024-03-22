import heapq
from cmath import inf
from collections import deque
from typing import List


class Solution:
    # dp超时
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        dp = [[inf] * len(grid[0]) for _ in range(len(grid))]
        dp[0][0] = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for k in range(1, grid[i][j] + 1):
                    if j + k < len(grid[0]):
                        dp[i][j + k] = min(dp[i][j + k], dp[i][j] + 1)
                    if i + k < len(grid):
                        dp[i + k][j] = min(dp[i + k][j], dp[i][j] + 1)
        return dp[-1][-1] if dp[-1][-1] != inf else -1

    # bfs 超时
    def minimumVisitedCells1(self, grid: List[List[int]]) -> int:
        if len(grid) * len(grid[0]) == 1 and grid[0][0] == 0:
            return 1
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        cnt = 1
        queue = deque([(0, 0)])
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for k in range(1, grid[i][j] + 1):
                    if j + k < len(grid[0]) and not visited[i][j + k]:
                        visited[i][j + k] = True
                        queue.append((i, j + k))
                    if i + k < len(grid) and not visited[i + k][j]:
                        visited[i + k][j] = True
                        queue.append((i + k, j))
                if visited[-1][-1]:
                    return cnt + 1
            cnt += 1
        return -1

    # 优先队列，最小堆，
    # 从 rowH最小堆 中找到一个 步数 值最小的，且可以到达第 j 列的数对。
    # 从 colH 中找到一个 步数 值最小的，且可以到达第 i 行的数对
    # 最小堆维护（步数，最远能到的i或j）
    def minimumVisitedCells2(self, grid: List[List[int]]) -> int:
        col_heaps = [[] for _ in range(len(grid[0]))]  # 每一列的最小堆，记录的行之间的跳跃
        for i, row in enumerate(grid):
            row_h = []  # 第i行的最小堆,因为是一行一行遍历，所以这里每次都初始化为空数组就行，记录的是列之间的跳跃
            for j, (g, col_h) in enumerate(zip(row, col_heaps)):  # 算i和j这个点时候，就需要把第i行和第j类的最小堆拿出来
                # 因为最小堆是按照步数排序的，所以可能存在步数很小，但是无法到达现在这一点的情况
                while row_h and row_h[0][1] < j:  # 无法到达第j类
                    heapq.heappop(row_h)
                while col_h and col_h[0][1] < i:  # 无法到达第i行
                    heapq.heappop(col_h)  # 弹出无用数据
                f = inf if i or j else 1  # 起点算一个格子
                if row_h:
                    f = row_h[0][0] + 1  # 从左边跳过来
                if col_h:
                    f = min(f, col_h[0][0] + 1)  # 从上边跳过来
                if g and f < inf:
                    heapq.heappush(row_h, (f, g + j))  # 经过的格子数，向右最远能到达的列
                    heapq.heappush(col_h, (f, g + i))  # 经过的格子数，向下最远能到达的行号
        return f if f < inf else -1  # 此时的 f 是在 (m-1, n-1) 处算出来的



Solution().minimumVisitedCells1(grid=[[3, 4, 2, 1], [4, 2, 3, 1], [2, 1, 0, 0], [2, 4, 0, 0]])
