def dfs(n, t1, t2):
    if n == 0 and t1 == 0 and t2 == 0: # 如果七个小孩每个人都分到了塘并且两种糖都被分完了
        return 1
    if n < 0 or t1 < 0 or t2 < 0:
        return 0
    cnt = 0
    for i in range(0, 6):
        for j in range(0, 6):
            if 2 <= i + j <= 5:
                cnt += dfs(n - 1, t1 - i, t2 - j)
    return cnt


print(dfs(7, 9, 16))  # 递归两种水果和7个小孩
