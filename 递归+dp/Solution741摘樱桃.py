from cmath import inf
from functools import cache
from typing import List


class Solution:
    # 不能遍历两次，计算两次的最大值，两个最大值相加不一定是总体最大值
    def cherryPickup(self, grid: List[List[int]]) -> int:
        path = []
        n = len(grid)
        cntm = 0
        pathm = []

        def dfs(x: int, y: int, cnt: int):
            path.append((x, y))
            if x > n - 1 or y > n - 1 or grid[x][y] == -1:
                return
            if grid[x][y] == 1:
                cnt += 1
            nonlocal cntm, pathm
            if x == n - 1 and y == n - 1 and cnt > cntm:
                cntm = cnt
                pathm = path.copy()  # 需要拷贝，不然就是引用会随着path变化
            dfs(x + 1, y, cnt)
            path.pop()
            dfs(x, y + 1, cnt)
            path.pop()

        dfs(0, 0, 0)
        if not pathm:
            return 0
        for x, y in pathm:
            grid[x][y] = 0
        res = cntm
        cntm = 0
        dfs(0, 0, 0)
        return res + cntm

    # 超出时间限制，遍历两条路径
    def cherryPickup1(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cntm = 0

        @cache
        def dfs(x1: int, y1: int, x2: int, y2: int, cnt: int):
            if x1 > n - 1 or y1 > n - 1 or grid[x1][y1] == -1 \
                    or x2 > n - 1 or y2 > n - 1 or grid[x2][y2] == -1:
                return
            nonlocal cntm
            if x1 == x2 and y1 == y2:
                if grid[x1][y1] == 1:
                    cnt += 1
            else:
                if grid[x1][y1] == 1:
                    cnt += 1
                if grid[x2][y2] == 1:
                    cnt += 1
            if x1 == n - 1 and y1 == n - 1 and x2 == n - 1 and y2 == n - 1 and cnt > cntm:
                cntm = cnt
            dfs(x1 + 1, y1, x2 + 1, y2, cnt)
            dfs(x1 + 1, y1, x2, y2 + 1, cnt)
            dfs(x1, y1 + 1, x2 + 1, y2, cnt)
            dfs(x1, y1 + 1, x2, y2 + 1, cnt)

        dfs(0, 0, 0, 0, 0)
        return cntm

    # https://leetcode.cn/problems/cherry-pickup/solutions/2766975/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-ruue/
    # 定义 dfs(t,j,k) 表示两人从 (0,0) 出发，都走了 t 步，分别走到 (t−j,j) 和 (t−k,k)，可以得到的樱桃个数的最大值。
    def cherryPickup2(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(t: int, j: int, k: int):
            # 递归条件，不能出界，不能访问-1格子
            if j < 0 or k < 0 or t - j < 0 or t - k < 0 or grid[t - j][j] < 0 or grid[t - k][k] < 0:
                return -inf
            if t == 0:
                return grid[0][0]
            return max(dfs(t - 1, j, k), dfs(t - 1, j, k - 1), dfs(t - 1, j - 1, k),
                       dfs(t - 1, j - 1, k - 1)) + grid[t - j][j] + (grid[t - k][k] if j != k else 0)

        n = len(grid)
        return max(dfs(n * 2 - 2, n - 1, n - 1), 0)

    # f[t][j][k] 的定义和 dfs(t,j,k) 的定义是一样的，都表示两人从 (0,0) 出发，都走了 t 步，分别走到 (t−j,j) 和 (t−k,k)，可以得到的樱桃个数的最大值。
    # 这种定义方式没有状态能表示递归边界，即 j=−1, k=−1 这种出界的情况。
    # 在每个 f[i] 的最左边和最上边各插入一排状态，那么其余状态全部向右和向下偏移一位，把 f[t][j][k] 改为 f[t][j+1][k+1]。
    # 修改后 f[t][j+1][k+1] 表示两人从 (0,0) 出发，都走了 t 步，分别走到 (t−j,j) 和 (t−k,k)，可以得到的樱桃个数的最大值。此时 f[t][0][⋅] 和 f[t][⋅][0] 就对应出界的情况了。
    def cherryPickup3(self, grid: List[List[int]]) -> int:
        n = len(grid)
        f = [[[-inf] * (n + 1) for _ in range(n + 1)] for _ in range(n * 2 - 1)]
        f[0][1][1] = grid[0][0]
        for t in range(1, n * 2 - 1):
            for j in range(max(t - n + 1, 0), min(t + 1, n)):  # 保证0≤i≤n−1 且 0≤j≤n−1
                if grid[t - j][j] < 0:
                    continue
                for k in range(j, min(t + 1, n)):
                    if grid[t - k][k] < 0:
                        continue
                    f[t][j + 1][k + 1] = max(f[t - 1][j + 1][k + 1], f[t - 1][j + 1][k], f[t - 1][j][k + 1],
                                             f[t - 1][j][k]) + grid[t - j][j] + (grid[t - k][k] if k != j else 0)
        return max(f[-1][n][n], 0)

    # 在计算 f[t] 时，只会用到 f[t−1]，不会用到比 t−1 更早的状态。
    def cherryPickup4(self, grid: List[List[int]]) -> int:
        n = len(grid)
        f = [[-inf] * (n + 1) for _ in range(n + 1)]
        f[1][1] = grid[0][0]
        for t in range(1, n * 2 - 1):
            for j in range(min(t, n - 1), max(t - n, -1), -1):
                for k in range(min(t, n - 1), j - 1, -1):
                    if grid[t - j][j] < 0 or grid[t - k][k] < 0:
                        f[j + 1][k + 1] = -inf
                    else:
                        f[j + 1][k + 1] = max(f[j + 1][k + 1], f[j + 1][k], f[j][k + 1], f[j][k]) + \
                                          grid[t - j][j] + (grid[t - k][k] if k != j else 0)
        return max(f[n][n], 0)


Solution().cherryPickup2(grid=[[0, 1, -1], [1, 0, -1], [1, 1, 1]])
Solution().cherryPickup1(
    grid=[[1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1]])
