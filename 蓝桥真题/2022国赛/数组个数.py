n = int(input())
b = list(map(int,input().split()))

N = 1000000007


res = 0
# 代表第一个位置可能的取值
for i in range(0,10):
    # 代表第二个位置可能的取值
    for j in range(0,10):
        # dp[k][x][y] 表示当第k个位置的最大值为x，第k-1位置的最大值为y时的方案数
        dp = [[[0] * 11 for _ in range(11)] for _ in range(n)]
        dp[1][i][j] = 1

        for k in range(2,n):
            # 遍历前一个位置最大值x
            for x in range(0,10):
                # 遍历前两个位置最大值y
                for y in range(0,10):
                    if not dp[k-1][x][y]:
                        continue
                    for z in range(0,10):
                        if k == n - 1:
                            if max(x,y,z) == b[k - 1] and max(y,z,i) == b[k] and max(z,i,j) == b[0]:
                                dp[k][y][z] = (dp[k][y][z] + dp[k - 1][x][y]) % N
                        else:
                            if max(x,y,z) == b[k - 1]:
                                dp[k][y][z] = (dp[k][y][z] + dp[k - 1][x][y]) % N

        for l in range(10):
            for p in range(10):
                res = (dp[n - 1][l][p] + res) % N
                                

print(res)
