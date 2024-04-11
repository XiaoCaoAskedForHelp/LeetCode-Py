import math
from typing import List


class Solution:
    # 超出时间限制
    def gcd(self, a, b):
        if b == 0: return a
        return self.gcd(b, a % b)

    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        def dfs(root: int, pre: int):
            for x, y in queue[::-1]:
                if self.gcd(nums[root], x) == 1:
                    ans[root] = y
                    break
            queue.append((nums[root], root))
            for i in g[root]:
                if i != pre:
                    dfs(i, root)
            queue.remove((nums[root], root))

        n = len(nums)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        ans = [-1] * n
        queue = [(1, -1)]
        dfs(0, -1)
        return ans

    # 最暴力的做法是，枚举 x 的所有祖先节点。但如果这棵树是一条链，枚举 x 的所有祖先节点需要 O(n) 的时间，每个点都这样枚举的话，总共需要 O(n2)的时间，太慢了
    # 所有节点的节点值都不超过 50，我们可以枚举 [1,50] 中与 nums[x] 互质的数。由于要计算的是「最近」祖先，对于节点值相同的祖先，只需枚举深度最大的。因此，对于节点 x，我们至多枚举它的 50 个祖先。这样总共只需要 O(nU) 的时间，其中 U=50
    # valDepth数组。其中valDepth[j]保存节点值等于j的最近祖先的深度。
    # valNodeId 数组。其中 valNodeId[j] 保存节点值等于 j 的最近祖先的节点编号。

    def getCoprimes1(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        MX = 51
        # 预处理，coprime保存[1,MX)中与i互质的所有元素
        coprime = [[j for j in range(1, MX) if math.gcd(i, j) == 1] for i in range(MX)]

        n = len(nums)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        ans = [0] * n
        val_depth_id = [(-1, -1)] * MX  # 包含节点的深度和节点编号

        def dfs(x: int, fa: int, depth: int):
            val = nums[x]
            # 计算与val互质的祖先节点值中，节点深度最大的节点编号
            ans[x] = max(val_depth_id[j] for j in coprime[val])[1]  # 比深度，然后取出最深的节点编号
            tmp = val_depth_id[val]  # 用于恢复现场
            val_depth_id[val] = (depth, x)  # 保存val对应的节点深度和节点编号
            for y in g[x]:
                if y != fa:
                    dfs(y, x, depth + 1)
            val_depth_id[val] = tmp  # 恢复现场

        dfs(0, -1, 0)
        return ans


print(Solution().getCoprimes1(nums=[2, 3, 3, 2], edges=[[0, 1], [1, 2], [1, 3]]))
