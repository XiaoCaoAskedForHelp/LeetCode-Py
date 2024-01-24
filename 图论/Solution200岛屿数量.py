from collections import deque
from typing import List


class Solution:
    # 深度优先搜索
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = 0
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    visited[i][j] = True
                    result += 1
                    self.dfs(grid, visited, i, j)

        return result

    def dfs(self, grid, visited, i, j):
        for direction in self.directions:
            nextx = i + direction[0]
            nexty = j + direction[1]
            if nextx < 0 or nextx >= len(grid) or nexty < 0 or nexty >= len(grid[0]):
                continue
            if not visited[nextx][nexty] and grid[nextx][nexty] == '1':
                visited[nextx][nexty] = True
                self.dfs(grid, visited, nextx, nexty)

    def numIslands1(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 四个方向
        result = 0

        def dfs(x, y):
            for d in dirs:
                nextx = x + d[0]
                nexty = y + d[1]
                if nextx < 0 or nextx >= m or nexty < 0 or nexty >= n:  # 越界了，直接跳过
                    continue
                if not visited[nextx][nexty] and grid[nextx][nexty] == '1':  # 没有访问过的同时是陆地的
                    visited[nextx][nexty] = True
                    dfs(nextx, nexty)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    visited[i][j] = True
                    result += 1  # 遇到没访问过的陆地，+1
                    dfs(i, j)  # 将与其链接的陆地都标记上 true

        return result

    def numIslands2(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        result = 0

        def dfs(x, y):
            if visited[x][y] or grid[x][y] == '0':
                return
            visited[x][y] = True
            for d in dirs:
                nextx = x + d[0]
                nexty = y + d[1]
                if nextx < 0 or nextx >= m or nexty < 0 or nexty >= n:
                    continue
                dfs(nextx, nexty)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    result += 1
                    dfs(i, j)
        return result

    def numIslands3(self, grid: List[List[str]]) -> int:
        res = 0

        def traversal(i, j):
            m = len(grid)
            n = len(grid[0])

            if i < 0 or j < 0 or i >= m or j >= n:
                return  # 越界了
            elif grid[i][j] == "2" or grid[i][j] == "0":
                return

            grid[i][j] = "2"
            traversal(i - 1, j)  # 往上走
            traversal(i + 1, j)  # 往下走
            traversal(i, j - 1)  # 往左走
            traversal(i, j + 1)  # 往右走

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    traversal(i, j)
        return res

    def __init__(self):
        self.dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    def numIslands4(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    res += 1
                    self.bfs(grid, visited, i, j)
        return res

    def bfs(self, grid, visited, i, j):
        q = deque()
        q.append((i, j))
        visited[i][j] = True
        while q:
            x, y = q.popleft()
            for k in range(4):
                nextx = x + self.dirs[k][0]
                nexty = y + self.dirs[k][1]
                if nextx < 0 or nextx >= len(grid) or nexty < 0 or nexty >= len(grid[0]):
                    continue
                if not visited[nextx][nexty] and grid[nextx][nexty] == '1':
                    q.append((nextx, nexty))
                    visited[nextx][nexty] = True


Solution().numIslands2(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])
