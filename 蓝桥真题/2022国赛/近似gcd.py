import math

n, g = map(int, input().split())
a = [0] + list(map(int, input().split()))

# 双指针，用一个指针i表示，表示以i为结尾的子数组修改一次后左端最远延伸到j
# 那么以i为结尾的子数组左端去任意的j ~ i-1都是满足条件的子数组
temp = 0  # 记录上一个坏数的位置
left = right = 1
res = 0
for right in range(1, n + 1):
    t = math.gcd(g, a[right])
    if t != g:  # 如果当前这个数不是g的倍数
        left = temp + 1  # left移到上一个坏数的下一位
        temp = right  # 更新坏数位置
    if right - left + 1 >= 2:
        res += right - left
print(res)
