from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.position = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 四个方向

    # 深度优先遍历，把可以通向边缘部分的 1 全部标记成 true
    def dfs(self, grid: List[List[int]], row: int, col: int) -> None:
        for current in self.position:
            newRow, newCol = row + current[0], col + current[1]
            # 索引下标越界
            if newRow < 0 or newRow >= len(grid) or newCol < 0 or newCol >= len(grid[0]):
                continue
            # 当前位置值不是 1 或者已经被访问过了
            if grid[newRow][newCol] == 0: continue
            grid[newRow][newCol] = 0  # 标记成已经访问过了
            self.dfs(grid, newRow, newCol)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        rowSize, colSize, ans = len(grid), len(grid[0]), 0
        # 搜索左边界和右边界，对值为 1 的位置进行深度优先遍历
        for row in range(rowSize):
            if grid[row][0] == 1:
                self.dfs(grid, row, 0)
            if grid[row][colSize - 1] == 1:
                self.dfs(grid, row, colSize - 1)
        # 搜索上边界和下边界，对值为 1 的位置进行深度优先遍历，但是四个角不需要，因为上面遍历过了
        for col in range(1, colSize - 1):
            if grid[0][col] == 1:
                self.dfs(grid, 0, col)
            if grid[rowSize - 1][col] == 1:
                self.dfs(grid, rowSize - 1, col)
        # 找出矩阵中值为 1 但是没有被标记过的位置，记录答案，不需要去搜索了
        for row in range(1, rowSize - 1):  # 因为四个边缘已经遍历过了，所以不需要再遍历了，并且四个边缘上因为dfs没有改变值，所以也不能遍历
            for col in range(1, colSize - 1):
                if grid[row][col] == 1:
                    ans += 1
        return ans

    # 广度优先遍历，把可以通向边缘部分的 1 全部标记成 true
    def bfs(self, grid: List[List[int]], queue: deque, visited: List[List[bool]]) -> None:
        while queue:
            curPos = queue.popleft()
            for current in self.position:
                row, col = curPos[0] + current[0], curPos[1] + current[1]
                # 索引下标越界
                if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]): continue
                # 当前位置值不是 1 或者已经被访问过了
                if grid[row][col] == 0 or visited[row][col]: continue
                visited[row][col] = True
                queue.append([row, col])

    def numEnclaves1(self, grid: List[List[int]]) -> int:
        rowSize, colSize, ans = len(grid), len(grid[0]), 0
        # 标记数组记录每个值为 1 的位置是否可以到达边界，可以为 True，反之为 False
        visited = [[False for _ in range(colSize)] for _ in range(rowSize)]
        queue = deque()  # 队列
        # 搜索左侧边界和右侧边界查找 1 存入队列
        for row in range(rowSize):
            if grid[row][0] == 1:
                visited[row][0] = True
                queue.append([row, 0])
            if grid[row][colSize - 1] == 1:
                visited[row][colSize - 1] = True
                queue.append([row, colSize - 1])
        # 搜索上边界和下边界查找 1 存入队列，但是四个角不用遍历，因为上面已经遍历到了
        for col in range(1, colSize - 1):
            if grid[0][col] == 1:
                visited[0][col] = True
                queue.append([0, col])
            if grid[rowSize - 1][col] == 1:
                visited[rowSize - 1][col] = True
                queue.append([rowSize - 1, col])
        self.bfs(grid, queue, visited)  # 广度优先遍历
        # 找出矩阵中值为 1 但是没有被标记过的位置，记录答案
        for row in range(rowSize):
            for col in range(colSize):
                if grid[row][col] == 1 and not visited[row][col]:
                    ans += 1
        return ans


grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
Solution().numEnclaves(grid)
