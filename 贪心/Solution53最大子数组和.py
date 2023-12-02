from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float('-inf')
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:
                result = count # 取区间累计的最大值
            if count <= 0:
                count = 0  # # 相当于重置最大子序起始位置，因为遇到负数一定是拉低总和
        return result
