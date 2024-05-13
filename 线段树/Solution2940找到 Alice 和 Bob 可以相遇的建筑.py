import heapq
from typing import List


class Solution:
    # 最大值线段树，问区间 [j+1,n−1] 中的大于 v=heights[i] 的最小下标
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n = len(heights)
        tree = [0] * (n * 4)

        def pushup(o: int):
            tree[o] = max(tree[o * 2], tree[o * 2 + 1])

        def build(o: int, l: int, r: int):
            if l == r:
                tree[o] = heights[l - 1]
                return
            m = (l + r) // 2
            build(o * 2, l, m)
            build(o * 2 + 1, m + 1, r)
            pushup(o)

        def query(o: int, l: int, r: int, L: int, v: int):
            if v >= tree[o]:  # 最大值<=v，没法找到>0的数
                return 0
            if l == r:
                return l  # 找到了
            m = (l + r) // 2
            if L <= m:
                pos = query(o * 2, l, m, L, v)
                if pos > 0:  # 找到了
                    return pos
            return query(o * 2 + 1, m + 1, r, L, v)

        build(1, 1, n)
        res = []
        for i, j in queries:
            if i > j:
                i, j = j, i
            # if i == j or heights[i] < heights[j]:
            if i == j:  # 写成这样也可以，后面的的条件会直接会包含在之后的查找中
                res.append(j)
            else:
                pos = query(1, 1, n, j + 1, heights[i])  # 这时候heights[i]就是两个中的较大值了
                res.append(pos - 1)  # 不存在时刚好得到-1
        return res

    # 最小堆，遍历到某个数的时候，可以查看最小堆中有哪些可以或得答案，然后在将这个下标需要查询的加入最小堆
    def leftmostBuildingQueries1(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        left = [[] for _ in heights]  # 每个下标需要查询的
        for qi, (i, j) in enumerate(queries):
            if i > j:
                i, j = j, i  # 保证i<=j
            if i == j or heights[i] < heights[j]:
                ans[qi] = j  # i 直接到 j
            else:
                left[j].append((heights[i], qi))  # j是答案的最小坐标，表示加入最小堆的时机

        h = []  # 最小堆
        for i, x in enumerate(heights):  # 从小到大枚举下标i
            while h and h[0][0] < x:
                ans[heapq.heappop(h)[1]] = i  # 可以跳到i（此时i是最小的）
            for p in left[i]:
                heapq.heappush(h, p)  # 后面才能回答
        return ans
