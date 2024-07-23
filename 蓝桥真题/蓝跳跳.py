# # 超时
# k, p, l = map(int, input().split())
#
# dp = [[0] * (l + 1) for i in range(k + 1)]  # 这一次跳k步的情况下，每一个长度的方案数
# # 就跳一步能到的设为1
# for i in range(1, k + 1):
#     dp[i][i] = 1
#
# mod = 20201114
# for j in range(2, l + 1):
#     for m in range(1, k + 1):
#         if m < p and j - m >= 0:
#             # 如果这一步跳的是小于p的步数，那么上一步无论是跳什么步数都可以，到j-m长度所有方案数之和
#             for s in range(1, k + 1):
#                 dp[m][j] = (dp[m][j] + dp[s][j - m]) % mod
#         if m >= p and j - m >= 0:
#             # 如果这一步跳的步数大于p，那么前一步只能跳小于p的步数
#             for s in range(1, p):
#                 dp[m][j] = (dp[m][j] + dp[s][j - m]) % mod
#
# res = 0
# for i in range(1, k + 1):
#     res = (res + dp[i][l]) % mod
# print(res)

# 超时dp
# k, p, l = map(int, input().split())
#
# dp = [[0] * (k + 1) for _ in range(l + 1)]
# dp[1][1] = 1
# mod = 20201114
# for i in range(2, l + 1):
#     for j in range(1, k + 1):
#         if i - j == 0:
#             dp[i][j] += 1
#         elif j >= p:  # 如果步长大于等于p，前一步只能<P
#             dp[i][j] += sum(dp[i - j][1:p]) % mod
#         else:
#             dp[i][j] += sum(dp[i - j]) % mod
# print(sum(dp[l]) % mod)

# 内存超限
# 创建一个双层的循环数组，0层存步长<p的方式个数，1层存步长<k+1方式个数
# k, p, l = map(int, input().split())
# dp = [[0] * 2 for i in range(l + 1)]
# dp[1][0] = 1 # 初始化长度为一只能走一步的方案
# dp[0][0] = 1
# mod = 20201114
# for i in range(2, l + 1):
#     for j in range(1, p):
#         if i - j < 0:
#             break
#         dp[i][0] += (dp[i - j][1] + dp[i - j][0]) % mod
#     for j in range(p, k + 1):
#         if i - j < 0:
#             break
#         dp[i][1] += dp[i - j][0] % mod
# print(sum(dp[l]) % mod)

# 运行超时
k, p, l = map(int, input().split())
dp = [[0] * 2 for i in range(k)]
dp[1][0] = 1  # 初始化长度为一只能走一步的方案
dp[0][0] = 1
mod = 20201114
for i in range(2, l + 1):
    tmp1, tmp2 = 0, 0
    for j in range(1, p):
        if i - j < 0:
            break
        tmp1 += (dp[(i - j) % k][1] + dp[(i - j) % k][0]) % mod
    for j in range(p, k + 1):
        if i - j < 0:
            break
        tmp2 += dp[(i - j) % k][0] % mod
    dp[i % k][0] = tmp1
    dp[i % k][1] = tmp2
print(sum(dp[l % k]) % mod)
