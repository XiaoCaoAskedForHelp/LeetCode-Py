# 对于某一位操作时，不会影响右边的数值，所以是从右往左操作
# 对每一位操作的次数在-9到+9之间，因为超过了10就会进1，不如直接在高位操作
# 每位数最多向前进一位，或者借一位
# dp[i,j] 表示i-n都已经相等了，j对上一位影响的三种状态0,-1,1
from math import inf

n = int(input())
a = input()
b = input()
dp = [[inf] * 3 for _ in range(n + 1)]
dp[n][1] = 0  # 使用0，1,3表示三种状态，1就表示没有进位
for i in range(n - 1, -1, -1):  # 遍历0~n-1的每一位
    for j in range(3):  # 这一位的进位为（0,1,2） - 1
        for k in range(-9, 10):  # 这一位上的操作次数
            for t in range(3):  # 上一位的进位对这一位的影响
                if ord(a[i]) + k + t - 1 - ord(b[i]) == (j - 1) * 10:   # 操作次数可以让这一位变为b[i],同时进位可以有三个状态
                    dp[i][j] = min(dp[i][j], dp[i + 1][t] + abs(k))
print(min(dp[0][0], dp[0][1], dp[0][2]))
