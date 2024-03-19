import math
from cmath import inf
from itertools import accumulate
from typing import List


class Solution:
    # dp超时
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[inf] * (n - k) for _ in range(k + 1)]  # 表示i，j范围内的最小值
        dp[k][0] = nums[k]
        for i in range(k, -1, -1):
            for j in range(0, n - k):
                if j - 1 >= 0:
                    dp[i][j] = min(nums[j + k], dp[i][j - 1])
                if i + 1 <= k:
                    dp[i][j] = min(nums[i], dp[i + 1][j])
        res = 0
        for i in range(0, k + 1):
            for j in range(0, n - k):
                res = max(res, (j + k - i + 1) * dp[i][j])
        return res

    # 双指针
    def maximumScore1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = k - 1, k + 1
        res = 0
        # 枚举k的值，不要通过left和right跟区域内最小值比较来移动
        # 需要的区域内的最小值，所以只要大的数就能被划入区域内
        for i in range(nums[k], 0, -1):
            while left >= 0 and nums[left] >= i:
                left -= 1
            while right < n and nums[right] >= i:
                right += 1
            res = max(res, (right - left - 1) * i)
        return res

    # 双指针优化，直接把最小值降成left和right中的最小值
    def maximumScore2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right, i = k - 1, k + 1, nums[k]
        res = 0
        while i != -1:
            while left >= 0 and nums[left] >= i:
                left -= 1
            while right < n and nums[right] >= i:
                right += 1
            res = max(res, (right - left - 1) * i)
            i = max((-1 if left == -1 else nums[left]), (-1 if right == n else nums[right]))
        return res


Solution().maximumScore1(nums=[1, 4, 3, 7, 4, 5], k=3)
