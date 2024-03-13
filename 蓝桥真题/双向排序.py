# 超时
# l, n = [int(i) for i in input().split(" ")]
# list = [i for i in range(1, l + 1)]
#
# for _ in range(n):
#     op, idx = [int(i) for i in input().split(" ")]
#     if op:  # 升序排序
#         list[idx - 1:] = sorted(list[idx - 1:])
#     else:  # 降序排序
#         list[:idx] = sorted(list[:idx], reverse=True)
#
# for i in list:
#     print(str(i), end=" ")

# n, m = map(int, input().split())
# stk = []  # 使用列表作为栈
# ans = [0] * (n + 1)  # 初始化答案数组
#
# for _ in range(m):
#     p, q = map(int, input().split())
#     if p == 0:  # 前缀操作
#         while stk and stk[-1][0] == 0:
#             q = max(q, stk.pop()[1])
#         while len(stk) >= 2 and stk[-2][1] <= q:
#             stk.pop()
#             stk.pop()
#         stk.append((0, q))
#     elif stk:  # 后缀操作
#         while stk and stk[-1][0] == 1:
#             q = min(q, stk.pop()[1])
#         while len(stk) >= 2 and stk[-2][1] >= q:
#             stk.pop()
#             stk.pop()
#         stk.append((1, q))
#
# k, l, r = n, 1, n
# for x, y in stk:
#     if x == 0:
#         while r > y and l <= r:
#             ans[r] = k
#             r -= 1
#             k -= 1
#     else:
#         while l < y and l <= r:
#             ans[l] = k
#             l += 1
#             k -= 1
#     if l > r:
#         break
#
# if len(stk) % 2 == 0:
#     while l <= r:
#         ans[r] = k
#         r -= 1
#         k -= 1
# else:
#     while l <= r:
#         ans[l] = k
#         l += 1
#         k -= 1
#
# for i in range(1, n + 1):
#     print(ans[i], end=' ')

n, m = map(int, input().split())
ops = []

for _ in range(m):
    p, q = map(int, input().split())
    if not p:
        while ops and ops[-1][0] == p:
            q = max(q, ops.pop()[1])  # 如果是连续的相同的操作，那么操作范围长覆盖掉操作范围短的,这样就会形成两种操作一个一的出现
        while len(ops) >= 2 and ops[-2][1] <= q:
            ops.pop()
            ops.pop()  # 操作比上一次的操作范围广，即使中间有另一种操作，也不影响最后的结果，可以直接省略
        ops.append((p, q))
    else:
        while ops and ops[-1][0] == p:
            q = min(q, ops.pop()[1])  # 如果是连续的相同的操作，那么操作范围长覆盖掉操作范围短的,这样就会形成两种操作一个一的出现
        while len(ops) >= 2 and ops[-2][1] >= q:
            ops.pop()
            ops.pop()  # 操作比上一次的操作范围广，即使中间有另一种操作，也不影响最后的结果，可以直接省略
        ops.append((p, q))

# 固定两边，逐步向里面固定
l, r, k = 1, n, n
ans = [0] * (n + 1)
for x, y in ops:
    if x == 0:
        while r > y and l <= r:
            ans[r] = k
            r -= 1
            k -= 1
    else:
        while l < y and l <= r:
            ans[l] = k
            l += 1
            k -= 1

if len(ops) % 2 == 0:
    while l <= r:
        ans[r] = k
        r -= 1
        k -= 1
else:
    while l <= r:
        ans[l] = k
        l += 1
        k -= 1

for i in range(1, n + 1):
    print(ans[i], end=" ")
