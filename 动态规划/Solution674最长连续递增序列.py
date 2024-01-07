from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        result = 1
        dp = [1] * len(nums)
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:  # 连续记录
                dp[i + 1] = dp[i] + 1
            result = max(result, dp[i + 1])
        return result

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_length = 1
        current_length = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 1

        return max_length
