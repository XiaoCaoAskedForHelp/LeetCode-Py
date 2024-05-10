from typing import List


class Solution:
    # 统计1的个数
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        tree = [0] * (n * 4)  # 记录区间上1的个数
        mark = [False] * (n * 4)  # 懒标记,用bool值就行，因为就两种状态

        def pushup(p):
            tree[p] = tree[p * 2] + tree[p * 2 + 1]

        def build(p, l, r):
            if l == r:
                tree[p] = nums1[l - 1]
            else:
                m = (l + r) // 2
                build(p * 2, l, m)
                build(p * 2 + 1, m + 1, r)
                pushup(p)

        def do(p, l, r):
            tree[p] = (r - l + 1) - tree[p]
            mark[p] = not mark[p]

        # [L,R]为翻转区间
        def update(p, l, r, L, R):
            if L <= l and r <= R:  # 如果当前区间在翻转区间之内
                do(p, l, r)
            else:  # 当前区间比翻转区间大,先pushdown在pushup
                m = (l + r) // 2
                if mark[p]:  # 原本应该是直接pushdown
                    do(2 * p, l, m)
                    do(2 * p + 1, m + 1, r)
                    mark[p] = False
                if m >= L:
                    update(p * 2, l, m, L, R)
                if m < R:
                    update(p * 2 + 1, m + 1, r, L, R)
                pushup(p)

        build(1, 1, n)
        ans = []
        s = sum(nums2)
        for x, l, r in queries:
            if x == 1:
                update(1, 1, n, l + 1, r + 1)
            elif x == 2:
                s += l * tree[1]  # 就是区间上所有的1，就是能加的大小
            else:
                ans.append(s)
        return ans
