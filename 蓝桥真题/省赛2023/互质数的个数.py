# 时间超限
# from collections import defaultdict
#
# # 欧拉函数，就能求出一个数所有比他小的互质数个数
# a, b = map(int, input().split())
# mod = 998244353
#
# # 先求出所有的质数
# dic = defaultdict(int)
# for i in range(2, a // 2 + 2):
#     while a % i == 0:
#         dic[i] += 1
#         a //= i
#
#
# def qpow(x: int, y: int):
#     ans = 1
#     while y:
#         if y & 1:
#             ans = (ans * x) % mod
#         x *= x
#         y >>= 1
#     return ans
#
#
# res = 1
# for k, v in dic.items():
#     # 欧拉函数公式（化简）   p^(n-1)*(p-1)的相乘
#     res = (res * qpow(k, v * b - 1)) % mod
#     res = (res * (k - 1)) % mod
# print(res)
import math

# 时间超限
# 使用筛法搞定质因子
# a, b = map(int, input().split())
# mod = 998244353
#
#
# def qpow(x: int, y: int):
#     ans = 1
#     while y:
#         if y & 1:
#             ans = (ans * x) % mod
#         x *= x
#         y >>= 1
#     return ans
#
#
# a1 = a
# ans = 1
# for i in range(2, a):
#     time = 0
#     while a % i == 0:
#         if time == 0:  # 求一个互质数的公式就是先乘比质数因子小的数，在乘n-1次质数因子
#             ans = ans * (i - 1) % mod
#             a //= i
#             time += 1
#         else:
#             ans = ans * i % mod
#             a //= i
#
# ans = ans * qpow(a1, b - 1) % mod
# print(ans)

# //由如上算法可知,n的欧拉函数只与其质因数的组成有关,与每个质因数的个数无关
# //对于不同的数字,只要它们的质因数组成相同,计算过程中就会除以相同的pi乘以相同的(pi-1)
# //故若m和n的质因数组成相同,m是n的k倍,则Euler(m)也是Euler(n)的k倍
# //而a^b是a的a^(b-1)倍,则由此推出Euler(a^b)=Euler(a)*(a^(b-1)),此即为最终答案

from math import sqrt, floor

# 请在此输入您的代码
M = 998244353


def phi(n: int) -> int:
    ans = n
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            ans = ans * (i - 1) // i
            while n % i == 0:
                n = n // i
    if (n > 1):
        ans = ans * (n - 1) // n
    return ans


def solve():
    a, b = (int(_) for _ in input().split(' '))
    ans = phi(a) * pow(a, b - 1, M) % M
    print(ans)


solve()
