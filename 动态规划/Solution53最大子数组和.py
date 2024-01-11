from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])  # 状态转移公式
            result = max(result, dp[i])  # result 保存dp[i]的最大值
        return result

    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[0]
        result = dp
        for i in range(1, len(nums)):
            dp = max(dp + nums[i], nums[i])
            result = max(result, dp)
        return result
