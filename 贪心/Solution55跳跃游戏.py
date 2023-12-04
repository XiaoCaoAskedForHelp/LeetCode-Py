from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        if len(nums) == 1: return True
        # python不支持动态修改for循环中变量,使用while循环代替
        for i in range(cover + 1):
            cover = max(cover, i + nums[i])
            if cover >= len(nums) - 1: return True
        return False

    def canJump1(self, nums: List[int]) -> bool:
        cover = 0
        if len(nums) == 1: return True
        i = 0
        while i <= cover:
            cover = max(cover, i + nums[i])
            if cover >= len(nums) - 1: return True
            i += 1
        return False

    def canJump2(self, nums: List[int]) -> bool:
        cover = 0
        if len(nums) == 1: return True
        for i in range(len(nums)):
            if i <= cover:
                cover = max(cover, i + nums[i])
                if cover >= len(nums) - 1: return True

        return False


nums = [2, 3, 1, 1, 4]
Solution().canJump(nums)
