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

# 时间超限
# 使用筛法搞定质因子
a, b = map(int, input().split())
mod = 998244353


def qpow(x: int, y: int):
    ans = 1
    while y:
        if y & 1:
            ans = (ans * x) % mod
        x *= x
        y >>= 1
    return ans


a1 = a
ans = 1
for i in range(2, a):
    time = 0
    while a % i == 0:
        if time == 0:
            ans = ans * (i - 1) % mod
            a //= i
            time += 1
        else:
            ans = ans * i % mod
            a //= i

ans = ans * qpow(a1, b - 1) % mod
print(ans)
