# https://www.bilibili.com/video/BV1v64y1P7mE
# dp[i−1]表示从高度i − 1出发到顶部花费的期望时间。
import math

n = int(input())
p = 998244353
res = 0


def qmi(a, b):
    res = 1
    while b:
        if b & 1:
            res = res * a % p
        a = a * a % p
        b >>= 1
    return res


while n:
    x, y = map(int, input().split())
    # res = (res + 1) * y % p * qmi(y - x, p - 2) % p
    res = (res + 1) * y % p * pow(y - x, p - 2, p) % p
    n -= 1
print(res)
