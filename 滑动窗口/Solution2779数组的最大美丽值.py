from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        end = 1
        res = 0
        while end < len(nums):
            if nums[end] <= nums[start] + 2 * k:
                end += 1
            else:
                res = max(end - start, res)
                while start < end and nums[end] > nums[start] + 2 * k:
                    start += 1  # start不能只能跳到end，而是应该找到满足条件的最小的start
                end += 1
        res = max(end - start, res)
        return res

    def maximumBeauty1(self, nums: List[int], k: int) -> int:
        # 题意相当于选出若干闭区间，这些区间的交集不为空
        nums.sort()
        ans = left = 0
        for right, x in enumerate(nums):
            while x - nums[left] > k * 2:
                left += 1
            ans = max(ans, right - left + 1)
        return ans


Solution().maximumBeauty([48, 93, 96, 19], 24)
