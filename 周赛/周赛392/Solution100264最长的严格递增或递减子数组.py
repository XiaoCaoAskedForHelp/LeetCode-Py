from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 1
        res = 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 1
        res = max(res, cnt)
        cnt = 1
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 1
        res = max(res, cnt)
        return res


print(Solution().longestMonotonicSubarray(nums=[3, 2, 1]))
