# 　　对于一个 n 行 m 列的矩阵，它的一个 k 行 k 列的子矩阵是指由矩阵中的连续 k 行、连续 k 列组成的矩阵。
# 　　子矩阵的和是指子矩阵中所有元素的和。现在，小蓝对于一个矩阵中的子矩阵中最大的子矩阵的和很感兴趣。
# 　　例如，对于如下 3 行 4 列的矩阵，2 行 2 列的子矩阵的和的最大值是 8，对应的子矩阵为由最后两行最后两列组成的子矩阵。
# 　　2 0 2 3
# 　　1 1 0 1
# 　　1 2 3 4
# 　　现在，小蓝有一个 30 行 20 列的大矩阵，如下所示，请问它的 5 行 5 列的子矩阵的和的最大值是多少？

matirx = []
with open('matrix', encoding='utf-8') as f:
    while f:
        read_data = f.readline()
        if not read_data:
            break
        matirx.append([int(i) for i in read_data.strip().split(" ")])

print(len(matirx), len(matirx[0]))

m = 0
for i in range(len(matirx) - 4):
    for j in range(len(matirx[0]) - 4):
        m = max(m, sum([matirx[i + m][j + n] for m in range(5) for n in range(5)]))

print(m)
