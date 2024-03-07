from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = -1
        need = [1, -1]
        index = 0
        i = 1
        while i < n:
            if nums[i] - nums[i - 1] == 1:
                while i < n and nums[i] - nums[i - 1] == need[index % 2]:
                    index += 1
                    i += 1
                res = max(res, index + 1)
                index = 0
                i -= 1
            i += 1
        return res if res != 1 else 0


Solution().alternatingSubarray([21, 9, 5])
Solution().alternatingSubarray([2, 3, 4, 3, 4])
