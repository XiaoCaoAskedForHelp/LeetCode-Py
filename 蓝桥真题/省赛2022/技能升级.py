## 运行超时
# import heapq
#
# n, m = map(int, input().split())
# queue = []
# for i in range(n):
#     sk, de = map(int, input().split())
#     heapq.heappush(queue, (-sk, de))
#
# ans = 0
# while m:
#     m -= 1
#     sk, de = heapq.heappop(queue)
#     sk = -sk
#     ans += sk
#     sk -= de
#     heapq.heappush(queue, (-sk, de))
#
# print(ans)

# 超时
# n, m = map(int, input().split())
# sks = []
# for i in range(n):
#     sk, de = map(int, input().split())
#     sks += [i for i in range(sk, 0, -de)]
#     if sk % de != 0:
#         sks.append(sk % de)
# sks.sort(reverse=True)
# print(sum(sks[:m]))

def check(mid):  # 最后一次技能升级为mid，之前所以的次数能不能到m
    cnt = 0
    for i in range(n):
        if a[i] < mid:
            continue  # 第i个技能的初始值还不够mid，不能用这个技能
        cnt += (a[i] - mid) // b[i] + 1  # 第i个技能用掉的次数
        if cnt >= m:  # 所有技能升级的总次数大于等于m次，说明mid设小了
            return True
    return False  # 小于m，说明mid设大了


n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
l, r = 1, 1000000  # 二分枚举最后一次攻击力最高能加多少
while l <= r:
    mid = (l + r) // 2
    if check(mid):  # 去统计mid之前有多少次增加攻击力能否到m
        l = mid + 1
    else:
        r = mid - 1  # r最大的最后一个数字能可以保证正好是>=mid的
attack = 0
cnt = m
for i in range(n):
    if a[i] <= r:
        continue
    t = (a[i] - l) // b[i] + 1  # 第 i 个技能的升级次数
    if a[i] - b[i] * (t - 1) == r:  # 这个技能没每次升级刚好等于r，其他技能更好
        t -= 1
    attack += (a[i] + a[i] - (t - 1) * b[i]) * t // 2
    cnt -= t
print(attack + cnt * r)  # cnt如果还>0,就用r来凑
