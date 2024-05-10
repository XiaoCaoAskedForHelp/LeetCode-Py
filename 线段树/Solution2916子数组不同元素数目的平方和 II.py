from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1Tz4y1N7Wx讲解    lazy线段树（维护区间[j+1,i]的和） + 子串统计
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        tree = [0] * (n * 4)
        mark = [0] * (n * 4)

        def do(o, l, r, add):
            tree[o] += add * (r - l + 1)
            mark[o] += add

        # 把[L,R]加一，同时返回加一之前的区间和
        def query_and_add(o, l, r, L, R):  # 先求和在加一，将两个步骤一起操作
            if L <= l and r <= R:
                res = tree[o]  # 先res暂未修改的
                do(o, l, r, 1)  # 在修改
                return res
            m = (l + r) // 2
            add = mark[o]
            if add:
                do(o * 2, l, m, add)
                do(o * 2 + 1, m + 1, r, add)
                mark[o] = 0  # 已经pushdown了，就将这个树节点的懒标记置为0
            res = 0
            if L <= m:
                res += query_and_add(o * 2, l, m, L, R)
            if m < R:
                res += query_and_add(o * 2 + 1, m + 1, r, L, R)
            tree[o] = tree[o * 2] + tree[o * 2 + 1]  # pushup
            return res

        ans = s = 0
        last = {}  # 记录上一次出现的位置
        for i, x in enumerate(nums, 1):
            j = last.get(x, 0)
            s += query_and_add(1, 1, n, j + 1, i) * 2 + i - j  # 用变量s维护右端点为i的子数组的不同计数的平方和  前面是线段树的操作
            ans += s
            last[x] = i
        return ans % (10 ** 9 + 7)
