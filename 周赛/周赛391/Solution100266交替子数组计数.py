from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        # 贪心求0101这种串的最大长度，数量就是等差数列，然后在加上其他相同的单个的数量
        # 双指针
        res = 0
        n = len(nums)
        start = 0
        end = 1
        cnt = 0  # 相邻元素值不相同的长度
        while end < n:
            while end < n and nums[end] != nums[end - 1]:
                end += 1
            if end != start + 1:
                l = end - start
                cnt += l
                res += (1 + l) * l // 2
                start = end - 1
            start += 1
            end += 1
        res += (n - cnt)  # 剩下那些相同的
        return res
