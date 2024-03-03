from cmath import inf
from typing import List


class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        n = len(grid)
        mid = n // 2
        dict = [0, 0, 0]
        # 算出拼成Y所用的0,1,2个数
        for i in range(mid):
            dict[grid[i][i]] += 1
            dict[grid[i][n - 1 - i]] += 1
            dict[grid[n - 1 - i][mid]] += 1

        dict[grid[mid][mid]] += 1

        dic = [0, 0, 0]
        for i in range(n):
            for j in range(n):
                dic[grid[i][j]] += 1

        op1 = []
        op2 = []
        for i in range(3):
            op1.append(sum(dict) - dict[i])
            tmp = dic[i] - dict[i]
            op2.append(sum(dic) - sum(dict) - tmp)

        res = inf
        for i in range(3):
            for j in range(3):
                if i != j:
                    res = min(res, op1[i] + op2[j])

        return res

    def minimumOperationsToWriteY1(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # 用下面这种方式直接遍历整个二位数组，不仅可以区分Y和其他，还可以统计0,1,2的个数，好写法
        # dict = [[0] * n] * 2
        dict = [[0] * n for _ in range(2)]
        flag = [[0] * n for _ in range(n)]
        for i in range(n // 2):
            flag[i][i] = 1
            flag[i][n - 1 - i] = 1
            flag[n - 1 - i][n // 2] = 1
        flag[n // 2][n // 2] = 1

        for i in range(n):
            for j in range(n):
                dict[flag[i][j]][grid[i][j]] += 1

        res = inf
        # 二维数组不能直接sum，只有一维数组可以。
        tot = sum(sum(g) for g in flag)
        for i in range(3):
            for j in range(3):
                if i != j:
                    cur = n * n - tot - dict[0][i] + tot - dict[1][j]
                    res = min(res, cur)

        return res


Solution().minimumOperationsToWriteY1([[1, 2, 2], [1, 1, 0], [0, 1, 0]])
