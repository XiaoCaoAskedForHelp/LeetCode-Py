import math

# 这样写会超出浮点数范围
# t = int(input())
# for _ in range(t):
#     n, m, k = map(int, input().split())
#     # 算出k属于树的第几层
#     layer = int(math.pow(k * (m - 1) + 1, 1 / m))
#     if (math.pow(m, layer) - 1) // (m - 1) != k:
#         layer += 1
#     # 树一共的层数
#     depth = int(math.pow(n * (m - 1) + 1, 1 / m))  # 可能会少一层
#     # 要计算的树的完整层数的节点个数
#     dep = depth - layer + 1
#     cnt = int((math.pow(m, dep) - 1) // (m - 1))
#     # 计算最后一层不完整的节点个数
#     first = k
#     end = k
#     for _ in range(dep):
#         first = m * first - (m - 2)
#         end = m * end + 1
#     if first <= n:
#         cnt += (end - first + 1) if end <= n else n - first + 1
#     print(cnt)


# 只通过20%
# t = int(input())
# for _ in range(t):
#     n, m, k = map(int, input().split())
#     cnt = 1
#     tmplayer = 1
#     layer = 1
#     while cnt < n:
#         if k <= cnt and layer == 1:
#             layer = tmplayer
#         cnt = m * cnt + 1
#         tmplayer += 1
#     depth = tmplayer if cnt == n else tmplayer - 1
#
#     # 要计算的树的完整层数的节点个数
#     dep = depth - layer + 1
#     cnt = int((math.pow(m, dep) - 1) // (m - 1))
#     if cnt == n:
#         print(cnt)
#         continue
#     # 计算最后一层不完整的节点个数
#     first = k
#     end = k
#     for _ in range(dep):
#         first = m * first - (m - 2)
#         end = m * end + 1
#     if first <= n:
#         cnt += (end - first + 1) if end <= n else n - first + 1
#     print(cnt)

# 下面是通过的
# t = int(input())
# for _ in range(t):
#     n, m, k = map(int, input().split())
#     l = k  # 表示子节点的左端点
#     r = k  # 表示子节点的右端点
#     ans = 1  # 记录总的节点数
#     res = 1  # 记录每一层子节点的数量
#     while r * m + 1 <= n:  # 如果子节点最右端小于n，说明没到尽头
#         res *= m  # 计算这一层的所有子节点数量
#         ans += res  # 更新总节点数量
#         l = l * m - (m - 2)  # 更新左端点
#         r = r * m + 1  # 更新右端点
#     l = l * m - (m - 2)  # 最后一层最左端点
#     r = r * m + 1  # 最后一层最右端点
#     ans += max(0, min(n, r) - l + 1)  # 最后一层最右端点就是n，直接用n-l+1计算成这层的节点个数
#     print(ans)
