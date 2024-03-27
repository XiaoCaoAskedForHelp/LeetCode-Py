from typing import List


class Solution:
    def qpow(self, a: int, b: int):
        mod = 10 ** 9 + 7
        res = 1
        while b:
            if b & 1:
                res = (res * a) % mod
            a = (a * a) % mod
            b >>= 1
        return res

    def countWays(self, ranges: List[List[int]]) -> int:
        # 先将区间合并，统计出区间个数，然后得出结果
        ranges.sort(key=lambda range: range[0])
        cnt = 0
        left, right = -1, -1
        for x, y in ranges:
            if x > right:
                left = x
                right = y
                cnt += 1
            else:
                right = max(y, right)
        # 结果是组合数
        return self.qpow(2, cnt)

    def countWays1(self, ranges: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        ranges.sort()
        n = len(ranges)
        res = 1
        i = 0
        while i < n:
            r = ranges[i][1]
            j = i + 1
            while j < n and ranges[j][0] <= r:
                r = max(r, ranges[j][1])
                j += 1
            res = (res * 2) % mod
            i = j
        return res


Solution().countWays(ranges=[[0, 0], [8, 9], [12, 13], [1, 3]])
