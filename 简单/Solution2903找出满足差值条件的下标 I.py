from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + indexDifference, n):
                if abs(nums[i] - nums[j]) >= valueDifference:
                    return [i, j]

        return [-1, -1]

    def findIndices1(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        max_idx = min_idx = 0  # 记录i的出现的最大值和最小值
        for j in range(indexDifference, len(nums)):
            i = j - indexDifference
            if nums[i] > nums[max_idx]:
                max_idx = i
            if nums[i] < nums[min_idx]:
                min_idx = i
            if nums[max_idx] - nums[j] >= valueDifference:
                return [max_idx, j]
            if nums[j] - nums[min_idx] >= valueDifference:
                return [min_idx, j]
        return [-1, -1]
