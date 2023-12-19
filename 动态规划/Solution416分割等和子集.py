from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = 0
        # dp[i]中的i表示背包内总和
        # 题目中说：每个数组中的元素不会超过 100，数组的大小不会超过 200
        dp = [0] * 10001

        for num in nums:
            _sum += num

        # 也可以使用内置函数一步求和
        # _sum = sum(nums)

        if _sum % 2 == 1:
            return False
        target = _sum // 2

        # 0-1背包
        for num in nums:
            # 每一个元素一定是不可重复放入，所以从大到小遍历
            for j in range(target, num - 1, -1):
                dp[j] = max(dp[j], dp[j - num] + num)

        # 集合中的元素正好可以凑成总和target
        if dp[target] == target:
            return True
        return False

    def canPartition1(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        dp = [0] * (target + 1)
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = max(dp[j], dp[j - num] + num)
        return dp[-1] == target

    def canPartition2(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2
        dp = [[False] * (target_sum + 1) for _ in range(len(nums) + 1)]

        # 初始化第一行（空子集可以得到和为0）
        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(1, target_sum + 1):
                if j < nums[i - 1]:
                    # 当前数字大于目标和时，无法使用该数字
                    dp[i][j] = dp[i - 1][j]
                else:
                    # 当前数字小于等于目标和时，可以选择使用或不使用该数字
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[len(nums)][target_sum]


    def canPartition3(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2
        dp = [False] * (target_sum + 1)
        dp[0] = True

        for num in nums:
            # 从target_sum逆序迭代到num，步长为-1
            for i in range(target_sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target_sum]
