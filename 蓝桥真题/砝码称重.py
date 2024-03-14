from collections import deque

n = int(input())

weights = [int(i) for i in input().split()]

# 集合加数组
# st = set()
#
# for w in weights:
#     nums = list(st)
#     for i in nums:
#         st.add(w + i)
#         if abs(i - w) != 0:
#             st.add(abs(i - w))   # 这一步很神奇，你能想到就很简单，通过abs取绝对值，就能取到w-i的情况
#     st.add(w)
# print(len(st))


# 动态规划
# dp[i][j] 代表的是 “装入前 i 个砝码后，能否凑成重量为 j 的情况，能凑成的话，值就为 true，否则为 false”。
# s = sum(weights)  # 最大能生成的数字
# dp = [[False] * (s + 1) for _ in range(2)]  # 新加一个数，就更新一个能凑成的数
#
# for i, w in enumerate(weights):
#     for j in range(1, s + 1):
#         # 情况一就是砝码本身，情况二通过前后的数减法得到，情况三通过加法得到
#         dp[(i + 1) % 2][j] = dp[i % 2][j] or w == j or dp[i % 2][abs(j - w)] or (
#             dp[i % 2][j + w] if j + w <= sum(weights) else False)
# res = 0
# for i in range(1, s + 1):
#     if dp[n % 2][i]:
#         res += 1
# print(res)

# bfs
queue = deque([0])
ans = [False] * (sum(weights) + 1)
cnt = 0
for w in weights:
    l = len(queue)
    while l:
        num = queue.popleft()
        if not ans[num + w]:
            ans[num + w] = True  # 加上这个数字可以拼成的数
            queue.append(num + w)
            cnt += 1
        if not ans[w]:
            ans[w] = True
            queue.append(w)
            cnt += 1
        if not ans[abs(num - w)]:
            ans[abs(num - w)] = True
            queue.append(abs(num - w))
            cnt += 1
        l -= 1
        queue.append(num)  # 得把原来的数放回去

if ans[0]:
    print(str(cnt - 1))
else:
    print(str(cnt))
