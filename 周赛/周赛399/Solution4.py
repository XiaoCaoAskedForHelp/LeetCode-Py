from cmath import inf
from typing import List


class Solution:
    # 不包含相邻元素的子序列
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        mx = [0] * (n * 4)

        # margin = [[False, False]] * (n * 4)

        def pushup(o: int, m: int):
            # if not margin[o * 2][1] or not margin[o * 2 + 1][0]:
            mx[o] = max(mx[o * 2], 0) + max(mx[o * 2 + 1], 0)

        # elif margin[o * 2][1] and margin[o * 2 + 1][0]:
        #     mi = inf
        #     flag = True
        #     if mx[o * 2] > 0:
        #         mx[o] += mx[o * 2]
        #         mi = min(nums[m - 1], mi)
        #     else:
        #         flag = False
        #     if mx[o * 2 + 1] > 0:
        #         mx[o] += mx[o * 2 + 1]
        #         mi = min(nums[m], mi)
        #     else:
        #         flag = False
        #     if flag:
        #         mx[o] -= max(0, mi)
        #
        # margin[o][0] = margin[o * 2][0]
        # margin[o][1] = margin[o * 2 + 1][1]

        def build(o: int, l: int, r: int):
            if l == r:
                mx[o] = nums[l - 1]
                # margin[o][0] = True
                # margin[o][1] = True
            else:
                m = (l + r) // 2
                build(o * 2, l, m)
                build(o * 2 + 1, m + 1, r)
                pushup(o, m)

        def update(o: int, l: int, r: int, pos: int, x: int):
            if l == r == pos:
                mx[o] = x
            else:
                m = (l + r) // 2
                if m >= pos:
                    update(o * 2, l, m, pos, x)
                else:
                    update(o * 2 + 1, m + 1, r, pos, x)
                pushup(o, m)

        build(1, 1, n)
        res = 0
        mod = 10 ** 9 + 7
        for pos, x in queries:
            update(1, 1, n, pos + 1, x)
            res = (res + mx[1]) % mod
        return res

    def maximumSumSubsequence1(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        # 4个数分别保存
        # f 00(A) 表示在 A 第一个数一定不选，最后一个数也一定不选的情况下，打家劫舍的答案。
        # f01(A) 表示在 A 第一个数一定不选，最后一个数可选可不选的情况下，打家劫舍的答案。
        # f10(A) 表示在 A 第一个数可选可不选，最后一个数一定不选的情况下，打家劫舍的答案。
        # f11(A) 表示在 A 第一个数可选可不选，最后一个数也可选可不选的情况下，打家劫舍的答案
        t = [[0] * 4 for _ in range(2 << n.bit_length())]

        def pushup(o: int):
            a, b = t[o * 2], t[o * 2 + 1]
            t[o] = [
                max(a[0] + b[2], a[1] + b[0]),  # f00 = fa00 + fb10 或 fa01 + fb00
                max(a[0] + b[3], a[1] + b[1]),
                max(a[2] + b[2], a[3] + b[0]),
                max(a[2] + b[3], a[3] + b[1])
            ]

        # 用nums初识化线段树
        def build(o: int, l: int, r: int):
            if l == r:
                t[o][3] = max(nums[l], 0)
                return
            m = (l + r) // 2
            build(o * 2, l, m)
            build(o * 2 + 1, m + 1, r)
            pushup(o)

        # 把nums[i] 改成 val
        def update(o: int, l: int, r: int, i: int, val: int):
            if l == r:
                t[o][3] = max(val, 0)
                return
            m = (l + r) // 2
            if i <= m:
                update(o * 2, l, m, i, val)
            else:
                update(o * 2 + 1, m + 1, r, i, val)
            pushup(o)

        build(1, 0, n - 1)
        ans = 0
        for i, x in queries:
            update(1, 0, n - 1, i, x)
            ans += t[1][3]  # f11没有限制，也就是整个数组的打家劫舍
        return ans % 1_000_000_007


Solution().maximumSumSubsequence(nums=[0, 3, 3, 3, 1, -2], queries=[[4, 0], [1, 0]])
Solution().maximumSumSubsequence(nums=[3, 5, 9], queries=[[1, -2], [0, -3]])
Solution().maximumSumSubsequence(nums=[0, -1], queries=[[0, -5]])
