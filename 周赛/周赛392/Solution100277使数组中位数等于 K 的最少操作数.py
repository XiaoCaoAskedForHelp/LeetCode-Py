from typing import List


class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        mid = n // 2
        cnt = 0
        if nums[mid] == k:
            return 0
        elif nums[mid] > k:  # 需要减少
            for i in range(mid, -1, -1):
                if nums[i] > k:
                    cnt += (nums[i] - k)
        else:
            for i in range(mid, n):
                if nums[i] < k:
                    cnt += (k - nums[i])
        return cnt


print(Solution().minOperationsToMakeMedianK(nums = [1,2,3,4,5,6], k = 4))
