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

n, m = map(int, input().split())
stk = []  # 使用列表作为栈
ans = [0] * (n + 1)  # 初始化答案数组

for _ in range(m):
    p, q = map(int, input().split())
    if p == 0:  # 前缀操作
        while stk and stk[-1][0] == 0:
            q = max(q, stk.pop()[1])
        while len(stk) >= 2 and stk[-2][1] <= q:
            stk.pop()
            stk.pop()
        stk.append((0, q))
    elif stk:  # 后缀操作
        while stk and stk[-1][0] == 1:
            q = min(q, stk.pop()[1])
        while len(stk) >= 2 and stk[-2][1] >= q:
            stk.pop()
            stk.pop()
        stk.append((1, q))

k, l, r = n, 1, n
for x, y in stk:
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
    if l > r:
        break

if len(stk) % 2 == 0:
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
    print(ans[i], end=' ')

