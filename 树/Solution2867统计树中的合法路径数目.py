import math
from typing import List

# 以质数节点为根，用「深度优先搜索」的方式，递归搜索所有的非质数的子树，并求出所有子树的大小，
# 搜索过程中只搜索非质数节点。任何两个来自不同子树的节点，其路径都通过质数根节点，
# 路径上恰好只有根节点一个质数节点，根据题意路径是合法的。我们只需要把所子树大小，两两相乘并求和，
# 就可以得到包含根节点的所有合法路径。

# 埃氏筛
N = 10 ** 5 + 1
is_prime = [True] * N
is_prime[0] = is_prime[1] = False
for i in range(2, int(math.sqrt(N))):
    if is_prime[i]:
        for j in range(i * i, N, i):
            is_prime[j] = False


class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        # 每个节点连接的点集合
        g = [[] for _ in range(n + 1)]
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)

        nodes = []

        # pre防止递归重复
        def dfs(i, pre):
            nodes.append(i)
            for j in g[i]:
                if j != pre and not is_prime[j]:
                    dfs(j, i)

        ans = 0
        # 搜索每一个质数节点
        size = [0] * (n + 1)
        for i in range(1, n + 1):
            # 跳过非质数
            if not is_prime[i]:
                continue

            s = 0  # 记录已有非质数块的大小
            for j in g[i]:
                if is_prime[j]:
                    continue
                # 没有计算过则dfs搜索
                if size[j] == 0:
                    nodes.clear()
                    dfs(j, -1)
                    # 每一块非质数字数大小记录下来
                    for node in nodes:
                        size[node] = len(nodes)
                # 这 size[y] 个非质数与之前遍历到的 s 个非质数，两两之间的路径只包含质数 x（i这个质数在路径中）
                ans += s * size[j]
                s += size[j]
            ans += s  # 加上从i这个根节点出发的路径（i这个根节点在路径两端）
        return ans

    # 由于 i 已经是质数，如果 i 是路径的一个端点，那么我们只需要累计与节点 i 相邻的所有连通分量的大小即可。
    # 如果 i 是路径上的某个中间点，那么我们需要累计相邻的任意两个连通分量的大小之积。
    def countPaths1(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        father = list(range(n + 1))
        size = [1] * (n + 1)

        def find(u):
            if father[u] != u:
                father[u] = find(father[u])  # 让节点u的父节点变为根节点
            return father[u]

        def join(u, v):
            pa, pb = find(u), find(v)
            if pa == pb:
                return
            if size[pa] > size[pb]:
                father[pb] = pa
                size[pa] += size[pb]
            else:
                father[pa] = pb
                size[pb] += size[pa]

        # 如果一条边的两个节点都不是质数，那么我们就将这两个节点合并到同一个连通分量中
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            if not is_prime[u] and not is_prime[v]:
                join(u, v)

        ans = 0
        for i in range(1, n + 1):
            if not is_prime[i]:
                continue
            t = 0
            for j in g[i]:
                if not is_prime[j]:
                    cnt = size[find(j)]
                    ans += t * cnt  # i为路径上的某个中间点
                    ans += cnt  # i为路径上的端点
                    t += cnt
        return ans


Solution().countPaths(2, [[1, 2]])
