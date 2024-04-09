import collections
from bisect import bisect_left, bisect_right
from typing import List

from sortedcontainers import SortedList


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        cnt1 = 0
        cnt2 = 0
        for i in nums:
            if i < 0:
                cnt1 += 1
            elif i > 0:
                cnt2 += 1
        return max(cnt1, cnt2)

    def maximumCount1(self, nums: List[int]) -> int:
        nums = SortedList(nums)
        idx1 = nums.bisect_left(0)
        idx2 = nums.bisect_right(0)
        return max(idx1, len(nums) - idx2)

    def maximumCount2(self, nums: List[int]) -> int:
        neg = bisect_left(nums, 0)
        pos = len(nums) - bisect_right(nums, 0)
        return max(neg, pos)


Solution().maximumCount1(nums=[-3, -2, -1, 0, 0, 1, 2])
