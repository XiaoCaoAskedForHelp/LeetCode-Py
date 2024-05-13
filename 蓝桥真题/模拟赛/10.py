# 小蓝要上一个楼梯，楼梯共有 n 级台阶（即小蓝总共要走 n 级）。小蓝每一步可以走 a 级、b 级或 c 级台阶。
# 　　请问小蓝总共有多少种方案能正好走到楼梯顶端？

n = int(input())
a, b, c = [int(i) for i in input().split(" ")]

dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n + 1):
    dp[i] = (dp[i - a] if i - a >= 0 else 0) + (dp[i - b] if i - b >= 0 else 0) + (dp[i - c] if i - c >= 0 else 0)

print(dp[-1])
