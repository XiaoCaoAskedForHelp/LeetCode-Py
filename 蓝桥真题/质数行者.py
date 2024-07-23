# n3动态规划

n, m, w = map(int, input().split())
r1, c1, h1, r2, c2, h2 = map(int, input().split())

maxw = max(n, m, w)
is_Prime = [True] * (maxw + 1)
for i in range(2, (maxw + 1) // 2 + 1):
    if is_Prime[i]:
        for j in range(i * i, maxw + 1, i):
            is_Prime[j] = False
primes = [i for i in range(2, maxw + 1) if is_Prime[i]]

mod = 10 ** 9 + 7
dp = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(w + 1)]
dp[1][1][1] = 1
for z in range(1, w + 1):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if not ((i == r1 and j == c1 and z == h1) or (i == r2 and j == c2 and z == h2)):
                # 可以朝三个方向走
                for p in primes:
                    if z - p > 0 and (
                    not ((i == r1 and j == c1 and z - p == h1) or (i == r2 and j == c2 and z - p == h2))):
                        dp[z][i][j] = (dp[z][i][j] + dp[z - p][i][j]) % mod
                    if i - p > 0 and (
                    not ((i - p == r1 and j == c1 and z == h1) or (i - p == r2 and j == c2 and z == h2))):
                        dp[z][i][j] = (dp[z][i][j] + dp[z][i - p][j]) % mod
                    if j - p > 0 and (
                    not ((i == r1 and j - p == c1 and z == h1) or (i == r2 and j - p == c2 and z == h2))):
                        dp[z][i][j] = (dp[z][i][j] + dp[z][i][j - p]) % mod
print(dp[-1][-1][-1])


