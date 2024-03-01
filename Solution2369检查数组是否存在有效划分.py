from functools import cache
from typing import List


class Solution:
    # 超出时间限制
    def validPartition(self, nums: List[int]) -> bool:
        def partition(i):
            if i > len(nums): return False
            if i == len(nums): return True
            p1 = p2 = p3 = False
            if i + 1 < len(nums) and nums[i] == nums[i + 1]:
                p1 = partition(i + 2)
            if i + 2 < len(nums) and nums[i] == nums[i + 1] == nums[i + 2]:
                p2 = partition(i + 3)
            if i + 2 < len(nums) and nums[i + 1] - nums[i] == nums[i + 2] - nums[i + 1] == 1:
                p3 = partition(i + 3)
            return p1 or p2 or p3

        return partition(0)

    # dp[i]表示前i个元素组成的数组是否至少存在一个有效划分。边界情况dp[0]恒为true，而dp[n]即为结果。

    def validPartition1(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            if i >= 2:
                dp[i] = dp[i - 2] and self.validTwo(nums[i - 2], nums[i - 1])
            if i >= 3:
                dp[i] = dp[i] or (dp[i - 3] and self.validThree(nums[i - 3], nums[i - 2], nums[i - 1]))
        return dp[-1]

    def validTwo(self, num1, num2):
        return num2 == num1

    def validThree(self, num1, num2, num3):
        return (num1 == num2 == num3) or (num1 + 2 == num2 + 1 == num3)

    # 记忆化递归
    def validPartition2(self, nums: List[int]) -> bool:
        @cache
        def dfs(i: int) -> bool:
            if i >= n:
                return True
            a = i + 1 < n and nums[i] == nums[i + 1]
            b = i + 2 < n and nums[i] == nums[i + 1] == nums[i + 3]
            c = i + 2 < n and nums[i + 1] - nums[i] == nums[i + 2] - nums[i + 1] == 1
            return (a and dfs(i + 2)) or ((b or c) and dfs(i + 3))

        n = len(nums)
        return dfs(0)

    def validPartition3(self, nums: List[int]) -> bool:
        def dfs(i: int) -> bool:
            if i >= n:
                return True
            if f[i] != -1:
                return f[i]  # f[i] 表示0-i是否有正确的划分
            a = i + 1 < n and nums[i] == nums[i + 1]
            b = i + 2 < n and nums[i] == nums[i + 1] == nums[i + 2]
            c = i + 2 < n and nums[i + 1] - nums[i] == nums[i + 2] - nums[i + 1] == 1
            f[i] = ((a and dfs(i + 2)) or ((b or c) and dfs(i + 3)))
            return f[i]

        n = len(nums)
        f = [-1] * n
        return dfs(0)

    def validPartition4(self, nums: List[int]) -> bool:
        n = len(nums)
        f = [True] + [False] * n
        for i, x in enumerate(nums, 1):
            a = i - 2 >= 0 and nums[i - 2] == x
            b = i - 3 >= 0 and \
                ((x == nums[i - 2] == nums[i - 3])
                 or (nums[i - 3] + 2 == nums[i - 2] + 1 == x))
            f[i] = (a and f[i - 2]) or (b and f[i - 1])
        return f[n]


Solution().validPartition3([4, 4, 5, 6])
# Solution().validPartition([803201, 803201, 803201, 803201, 803202, 803203])
