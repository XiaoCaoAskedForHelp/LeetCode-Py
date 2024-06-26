from functools import cache
from typing import List


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        g = [set() for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0):
                    g[i].add(j)
                    g[j].add(i)

        @cache
        def dfs(i, visited, cnt):
            if cnt == n:
                return 1
            res = 0
            visited = list(visited)
            for j in g[i]:
                if not visited[j]:
                    visited[j] = True
                    res += dfs(j, tuple(visited), cnt + 1)
                    visited[j] = False  # 需要回撤
            return res

        res = 0
        mod = 10 ** 9 + 7
        for i in range(n):
            visited = [False] * n
            visited[i] = True
            res += dfs(i, tuple(visited), 1) % mod
        return res % mod

    # 用二进制表示集合
    def specialPerm1(self, nums: List[int]) -> int:
        # 定义 dfs(S,i) 表示在可以选的下标集合为 S，上一个选的数的下标是 i 时，可以构造出多少个特别排列。
        # 枚举当前要选的数的下标 j，那么接下来要解决的问题是，在可以选的下标集合为 S∖{j}，上一个选的数的下标是 j 时，可以构造出多少个特别排列。
        @cache
        def dfs(s: int, i: int):
            if s == 0:
                return 1  # 找到一个特别的排列
            res = 0
            pre = nums[i]
            for j, x in enumerate(nums):
                if s >> j & 1 and (pre % x == 0 or x % pre == 0):
                    res += dfs(s ^ (1 << j), j)
            return res

        n = len(nums)
        u = (1 << n) - 1  # 使用二进制数来表示集合
        mod = 10 ** 9 + 7
        return sum(dfs(u ^ (1 << i), i) for i in range(n)) % mod

    def specialPerm2(self, nums: List[int]) -> int:
        # f[S][i] 的定义和 dfs(S,i) 的定义是一样的，都表示在可以选的下标集合为 S，上一个选的数的下标是 i 时，可以构造出多少个特别排列。
        n = len(nums)
        u = (1 << n) - 1
        f = [[0] * n for _ in range(u)]
        f[0] = [1] * n
        for s in range(1, u):
            for i, pre in enumerate(nums):
                if s >> i & 1:
                    continue
                for j, x in enumerate(nums):
                    if s >> j & 1 and (pre % x == 0 or x % pre == 0):
                        f[s][i] += f[s ^ (1 << j)][j]
        return sum(f[u ^ (1 << i)][i] for i in range(n)) % 1_000_000_007


Solution().specialPerm([20, 100, 50, 5, 10, 70, 7])
