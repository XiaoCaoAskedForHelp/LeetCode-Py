from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            flag = True
            for j in range(len(grid[0])):
                if i != j and grid[i][j] != 1:
                    flag = False
                    break
            if flag:
                return i
        return -1

    # 如果 grid[i] 有 n−1 个 1，即元素和为 n−1，那么 i 队就是冠军。
    def findChampion1(self, grid: List[List[int]]) -> int:
        for i, row in enumerate(grid):
            if sum(row) == len(grid) - 1:
                return i

    # 如果第 j 列的元素值都是 0，说明没有队伍可以击败 j 队，j 队是冠军。
    def findChampion2(self, grid: List[List[int]]) -> int:
        for j, col in enumerate(zip(*grid)):  # zip二维列表，相当于遍历每一列
            if 1 not in col:
                return j


Solution().findChampion2(grid=[[0, 0, 1], [1, 0, 1], [0, 0, 0]])
