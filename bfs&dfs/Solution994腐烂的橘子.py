from collections import deque
from typing import List


class Solution:
    # bfs
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
        ans = 0
        while queue:
            ans += 1
            l = len(queue)
            for _ in range(l):
                x, y = queue.popleft()
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    xx, yy = x + i, y + j
                    if xx < 0 or xx >= m or yy < 0 or yy >= n or grid[xx][yy] != 1:
                        continue
                    grid[xx][yy] = 2
                    queue.append((xx, yy))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return ans - 1 if ans != 0 else 0

    # 首先分别将腐烂的橘子和新鲜的橘子保存在两个集合中；
    # 模拟广度优先搜索的过程，方法是判断在每个腐烂橘子的四个方向上是否有新鲜橘子，如果有就腐烂它。每腐烂一次时间加 111，并剔除新鲜集合里腐烂的橘子；
    # 当橘子全部腐烂时结束循环。
    def orangesRotting1(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        rotten = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}  # 腐烂集合
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}  # 新鲜集合
        time = 0
        while fresh:
            if not rotten:
                return -1
            rotten = {(i + di, j + dj) for i, j in rotten for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)] if
                      (i + di, j + dj) in fresh}  # 即将腐烂的如果在新鲜的集合中，就将它腐烂
            fresh -= rotten  # 剔除腐烂的
            time += 1
        return time

    def orangesRotting2(self, grid: List[List[int]]) -> int:
        row, col, time = len(grid), len(grid[0]), 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j, time))
        # bfs
        while queue:
            i, j, time = queue.pop(0)
            for di, dj in directions:
                if 0 <= i + di < row and 0 <= j + dj < col and grid[i + di][j + dj] == 1:
                    grid[i + di][j + dj] = 2
                    queue.append((i + di, j + dj, time + 1))

        for row in grid:
            if 1 in row: return -1
        return time


Solution().orangesRotting(grid=[[1]])
Solution().orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]])
