from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = []
        for j in range(n):
            l = 0
            for i in range(m):
                l = max(l, len(str(grid[i][j])))
            res.append(l)

        return res

    def findColumnWidth1(self, grid: List[List[int]]) -> List[int]:
        res = []
        for nums in zip(*grid):
            res.append(max([len(str(i)) for i in nums]))
        return res

    def findColumnWidth2(self, grid: List[List[int]]) -> List[int]:
        return [max(len(str(x)) for x in col) for col in zip(*grid)]

    # 上述方法需要对每个数字都计算长度。但实际上，由于数字的绝对值越大，数字的长度就越长，所以只需要对每一列的最小值或最大值求长度。
    # 由于负数中的负号也算一个长度，我们可以取max(mx,−10⋅mn)
    def findColumnWidth3(self, grid: List[List[int]]) -> List[int]:
        return [len(str(max(max(col), -10 * min(col)))) for col in zip(*grid)]


Solution().findColumnWidth1(grid=[[1], [22], [333]])
