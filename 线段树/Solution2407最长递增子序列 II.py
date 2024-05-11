from typing import List


# 理解不深，还需要在看
class Solution:
    # f[i][j]表示从nums的前i个数中选择以元素j结尾的上升子序列的最长长度
    # 当 j != nums[i],f[i][j] = f[i-1][j]
    # 当 j == nums[i],f[i][j] = 1 + max(f[i-1][j'])    j-k <= j' < j
    # 因为i只依赖于i-1,所以其实只有一维
    # 等号左侧是单带修改    等号右侧是区间求max   => 线段树
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        u = max(nums)
        mx = [0] * (4 * u)

        # 单点修改,所以不需要lazy tag
        def modify(o: int, l: int, r: int, i: int, val: int):
            if l == r:
                mx[o] = val
                return
            m = (l + r) // 2
            if i <= m:
                modify(o * 2, l, m, i, val)
            else:
                modify(o * 2 + 1, m + 1, r, i, val)
            mx[o] = max(mx[o * 2], mx[o * 2 + 1])

        # 返回区间 [L,R] 内的最大值
        def query(o: int, l: int, r: int, L: int, R: int):  # L 和 R 在整个递归过程中均不变，将其大写，视作常量
            if L <= l and r <= R:
                return mx[o]
            res = 0
            m = (l + r) // 2
            if L <= m:
                res = query(o * 2, l, m, L, R)
            if R > m:
                res = max(res, query(o * 2 + 1, m + 1, r, L, R))
            return res

        for x in nums:
            if x == 1:
                modify(1, 1, u, 1, 1)
            else:
                res = 1 + query(1, 1, u, max(x - k, 1), x - 1)
                modify(1, 1, u, x, res)
        return mx[1]
