from functools import cache
from typing import List


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        # 分割或是不分割
        # dfs(i,j) a[i]  j = 0或1表示需不需要变号
        @cache
        def dfs(i: int, j:int):
            if i == len(nums):
                return 0
            # 分割需要变号，不分割变号和前一个相反
            return max(dfs(i + 1, 1) + nums[i], dfs(i + 1, j ^ 1) + (-nums[i] if j else nums[i]))

        return dfs(0, 0)


Solution().maximumTotalCost([-14, -13, -20])
