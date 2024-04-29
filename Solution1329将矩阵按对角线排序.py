from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i in range(n):
            x, y = 0, 0
            y = y + i
            xx, yy = x, y
            line = []
            while xx < m and yy < n:
                line.append(mat[xx][yy])
                xx += 1
                yy += 1
            line.sort()
            xx, yy = x, y
            while xx < m and yy < n:
                mat[xx][yy] = line[xx]
                xx += 1
                yy += 1
        for i in range(1, m):
            x, y = 0, 0
            x += i
            xx, yy = x, y
            line = []
            while xx < m and yy < n:
                line.append(mat[xx][yy])
                xx += 1
                yy += 1
            line.sort()
            xx, yy = x, y
            while xx < m and yy < n:
                mat[xx][yy] = line[yy]
                xx += 1
                yy += 1
        return mat

    # 设坐标为 (i,j)，设 k=i−j。
    # 第一条对角线上只有一个点，坐标为 (0,n−1)，其 k=1−n。
    # 最后一条对角线上也只有一个点，坐标为 (m−1,0)，其 k=m−1。
    # 所以枚举对角线，就是枚举 k 从 1−n 到 m−1。
    def diagonalSort1(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for k in range(1 - n, m):  # k = i - j
            # 最左边的行坐标就是0或者行坐标和纵坐标的差值，做右边的行坐标就是行最大值或者列坐标最大值减去差值
            left_i, right_i = max(k, 0), min(k + n, m)  # 只要知道行坐标就能推算出纵坐标
            a = sorted(mat[i][i - k] for i in range(left_i, right_i))
            for i in range(left_i, right_i):
                mat[i][i - k] = a[i - left_i]
        return mat

    # 依次遍历矩阵，将同一条对角线上的元素放在相同的数组内，对所有数组进行倒序排序，再重新遍历矩阵，将排序好的元素放回矩阵内。
    def diagonalSort2(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        diag = [[] for _ in range(m + n)]
        for i in range(m):
            for j in range(n):
                diag[i - j + n].append(mat[i][j])  # 从右上角到左上角分别是0-（m+n-1） 正好是i-j+列数
        for d in diag:
            d.sort(reverse=True)  # 从大道小排序，因为list只能从尾部取值
        for i in range(m):
            for j in range(n):
                mat[i][j] = diag[i - j + n].pop()
        return mat


Solution().diagonalSort(mat=[[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]])
