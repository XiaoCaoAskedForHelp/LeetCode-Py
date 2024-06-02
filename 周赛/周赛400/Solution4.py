import bisect
from cmath import inf
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = inf
        for i, x in enumerate(nums):
            ans = min(ans, abs(x - k))
            j = i - 1
            while j >= 0 and nums[j] & x != nums[j]:  # 后续的循环都无法让元素变小，退出内层循环
                nums[j] &= x
                ans = min(ans, abs(nums[j] - k))
                j -= 1
        return ans


Solution().minimumDifference(nums=[5, 13, 90, 92, 49], k=10)
Solution().minimumDifference(nums=[1, 2, 4, 5], k=3)
