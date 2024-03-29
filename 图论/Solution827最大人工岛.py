from collections import defaultdict
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        visited = set()  # 标记访问过的位置
        m, n = len(grid), len(grid[0])
        res = 0
        island_size = 0  # 用于保存当前岛屿的尺寸
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 四个方向
        islands_size = defaultdict(int)  # 保存每个岛屿的尺寸

        def dfs(island_num, r, c):
            visited.add((r, c))
            grid[r][c] = island_num  # 访问过的位置标记为岛屿编号
            nonlocal island_size
            island_size += 1
            for i in range(4):
                nextR = r + directions[i][0]
                nextC = c + directions[i][1]
                if (nextR not in range(m) or  # 行坐标越界
                        nextC not in range(n) or  # 列坐标越界
                        (nextR, nextC) in visited):  # 坐标已访问
                    continue
                if grid[nextR][nextC] == 1:  # 遇到有效坐标，进入下一个层搜索
                    dfs(island_num, nextR, nextC)

        island_num = 2  # 初始岛屿编号设为2， 因为grid里的数据有0和1， 所以从2开始编号
        all_land = True  #标记是否整个地图都是陆地
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    all_land = False   # 有海洋，标记为False
                if (r,c) not in visited and grid[r][c] == 1:
                    island_size = 0   #遍历每个位置前重置岛屿尺寸为0
                    dfs(island_num, r, c)
                    islands_size[island_num] = island_size  # 保存当前岛屿尺寸
                    island_num += 1  # 下一个岛屿编号加一

        if all_land:
            return m * n  # 如果全是陆地， 返回地图面积

        count = 0  # 某个位置0变成1后当前岛屿尺寸
        # 因为后续计算岛屿面积要往四个方向遍历，但某2个或3个方向的位置可能同属于一个岛，
        # 所以为避免重复累加，把已经访问过的岛屿编号加入到这个集合
        visited_island = set()  # 保存访问过的岛屿
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    count = 1  # 把由0转换为1的位置计算到面积里
                    visited_island.clear()  # 遍历每个位置前清空集合
                    for i in range(4):
                        nearR = r + directions[i][0]
                        nearC = c + directions[i][1]
                        if nearR not in range(m) or nearC not in range(n):  # 周围位置越界
                            continue
                        if grid[nearR][nearC] in visited_island:  # 岛屿已访问
                            continue
                        count += islands_size[grid[nearR][nearC]]  # 累加连在一起的岛屿面积
                        visited_island.add(grid[nearR][nearC])  # 标记当前岛屿已访问
                    res = max(res, count)
        return res