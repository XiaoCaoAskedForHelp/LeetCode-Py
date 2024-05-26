from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        ma = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ma[i][j] = matrix[i][j]
                if i > 0 and j > 0:
                    ma[i][j] ^= (ma[i][j - 1] ^ ma[i - 1][j] ^ ma[i - 1][j - 1])
                elif i > 0 and j == 0:
                    ma[i][j] ^= ma[i - 1][j]
                elif j > 0 and i == 0:
                    ma[i][j] ^= ma[i][j - 1]
                res.append(ma[i][j])
        res.sort(reverse=True)
        return res[k - 1]

    # s[i+1][j+1] 表示左上角在 (0,0)，右下角在 (i,j) 的子矩阵异或和
    def kthLargestValue1(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] ^ s[i][j + 1] ^ s[i][j] ^ x  # 避免了判断i==0和j==0的情况
        return sorted(x for row in s[1:] for x in row[1:])[-k]

    # 列前缀异或和
    # 计算 colSum[j]，表示第 j 列的当前遍历过的元素的异或和。
    def kthLargestValue1(self, matrix: List[List[int]], k: int) -> int:
        a = []
        col_sum = [0] * len(matrix[0])
        for row in matrix:
            s = 0  # 到i,j位置的异或总和
            for j, x in enumerate(row):
                col_sum[j] ^= x
                s ^= col_sum[j]
                a.append(s)
        a.sort()
        return a[-k]


Solution().kthLargestValue([[8, 10, 5, 8, 5, 7, 6, 0, 1, 4, 10, 6, 4, 3, 6, 8, 7, 9, 4, 2]], 2)
