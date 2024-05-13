# 给定一个字符矩阵，请找出能构成字母 Y 的最大长度，如果无法构成字母 Y，请输出 0 。

m, n = [int(i) for i in input().split(' ')]

matrix = []
for i in range(m):
    matrix.append(input())

print(len(matrix), len(matrix[0]))

res = 0
for i in range(1, m - 1):
    for j in range(1, n - 1):
        tmp = 1
        while i - tmp >= 0 and j - tmp >= 0 and j + tmp < n and i + tmp < m \
                and matrix[i][j] == matrix[i - tmp][j - tmp] == matrix[i - tmp][j + tmp] == matrix[i + tmp][j]:
            tmp += 1
        res = max(tmp - 1, res)
print(res)
