# 超时
# n = int(input())
# nums = [0] + list(map(int, input().split()))
#
#
# def gcd(a: int, b: int):
#     if b == 0:
#         return a
#     return gcd(b, a % b)
#
#
# for i in range(1, n + 1):
#     for j in range(i + 1, n + 1):
#         if gcd(nums[i], nums[j]) != 1:
#             print(i, j)
#             exit()
import math
from cmath import inf
from collections import defaultdict

# 有点反向操作的意思，通过质因子去联系数字
# 找出每个数的质因子用map存起来，key存质因子，val则是存储最小下标。
#  后续如果发现相同的质因子，则枚举该数字出现的质因子找最小下标
n = int(input())
nums = list(map(int, input().split()))

# 将Ai范围内的所有质因数都找到
is_prime = [True] * (10 ** 6 + 1)
i = 2
primes = []
while i * i <= len(is_prime):
    if is_prime[i]:
        primes.append(i)
        for j in range(i * i, len(is_prime), i):
            is_prime[j] = False
    i += 1

dic = defaultdict(int)
ans1, ans2 = inf, inf
for i, x in enumerate(nums, start=1):
    l = n + 1
    for j in primes:
        if j > x:
            break
        if x % j == 0:
            while x % j == 0:
                x //= j
            if dic[j]:
                l = min(l, dic[j])
            else:
                dic[j] = i
    # 超过根号max范围的质数
    if x > 1:
        if dic[x]:
            l = min(l, dic[x])
        else:
            dic[x] = i
    if l < ans1:
        ans1 = l
        ans2 = i
print(ans1, ans2)

# n = int(input())
# nums = list(map(int, input().split()))
#
#
# def update(factor, index):
#     global factors, i, j
#     if factor not in factors:
#         factors[factor] = index
#     else:
#         if factors[factor] == index:
#             return
#         new_i = min(index + 1, factors[factor] + 1)
#         new_j = max(index + 1, factors[factor] + 1)
#
#         if new_i < i or (new_i == i and new_j < j):
#             i = new_i
#             j = new_j
#
#
# max_prime = 10 ** 6
# is_prime = [True] * (max_prime + 2)
# primes = []
# i = 2
# # 因为是找质因数，i*i就行
# while i ** 2 <= max_prime:
#     if is_prime[i]:
#         primes.append(i)
#         for j in range(i * i, max_prime + 1, i):
#             is_prime[j] = False
#     i += 1
# i, j = [float("inf")] * 2
# factors = dict()
# for index, num in enumerate(nums):
#     if num == 1:
#         continue
#     # 质数
#     if num <= max_prime and is_prime[num]:
#         update(num, index)
#     else:
#         quotient = num
#         prime_index = 0
#         factor = primes[prime_index]
#         while factor ** 2 <= quotient:
#             if quotient % factor == 0:
#                 quotient //= factor
#                 update(factor, index)
#             else:
#                 prime_index += 1
#                 factor = primes[prime_index]
#         if quotient > 1:
#             update(quotient, index)
# print(f'{i} {j}')
