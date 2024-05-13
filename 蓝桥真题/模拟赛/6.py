# 小蓝要上一个楼梯，楼梯共有 n 级台阶（即小蓝总共要走 n 级）。小蓝每一步可以走 1 级、2 级或 3 级台阶。
# 　　请问小蓝至少要多少步才能上到楼梯顶端？
from cmath import inf

n = int(input())
dp = [inf] * (n + 1)
dp[0] = dp[1] = dp[2] = dp[3] = 1
for i in range(4, n + 1):
    dp[i] = min([dp[i - 3] + 1, dp[i - 2] + 1, dp[i - 1] + 1])

print(dp[-1])
