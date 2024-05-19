from itertools import accumulate, pairwise
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        sp = [False] * (n * 4)

        def pushup(o: int, l: int, r: int):
            m = (l + r) // 2
            midl = nums[m - 1] % 2
            midr = nums[m] % 2
            if midl == midr:
                sp[o] = False
            else:
                sp[o] = sp[o * 2] and sp[o * 2 + 1]

        def build(o: int, l: int, r: int):
            if l == r:
                sp[o] = True
                return
            m = (l + r) // 2
            build(o * 2, l, m)
            build(o * 2 + 1, m + 1, r)
            pushup(o, l, r)

        def query(o: int, l: int, r: int, L: int, R: int):
            if L <= l and r <= R:
                return sp[o]

            m = (l + r) // 2
            res = True
            if L <= m:
                res = res and query(o * 2, l, m, L, R)
            if R > m:
                res = res and query(o * 2 + 1, m + 1, r, L, R)
            if L <= m < R:
                res = res and (nums[m - 1] % 2 != nums[m] % 2)
            return res

        build(1, 1, n)
        res = []
        for l, r in queries:
            res.append(query(1, 1, n, l + 1, r + 1))
        return res

    # nums[i]mod2 不等于 nums[i+1]mod2 a[i]就设为0，反之设为1
    # 通过前缀和s 是否为0，判断子数组和是否为特征数组
    def isArraySpecial1(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        s = list(accumulate(((x ^ y ^ 1) & 1 for x, y in pairwise(nums)), initial=0))
        return [s[from_] == s[to] for from_, to in queries]


print(Solution().isArraySpecial(nums=[3, 4, 1, 2, 6], queries=[[0, 4]]))
print(Solution().isArraySpecial(nums=[4, 3, 1, 6], queries=[[0, 2], [2, 3]]))
