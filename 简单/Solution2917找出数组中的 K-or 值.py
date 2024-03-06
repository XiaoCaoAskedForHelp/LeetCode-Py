from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ks = [0 for i in range(50)]

        for num in nums:
            index = 0
            while num:
                ks[index] += num & 1
                num = num >> 1
                index += 1

        res = 0
        for i in range(50):
            if ks[i] >= k:
                res += 2 ** i
        return res

    def findKOr1(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(31):
            cnt = sum([1 for num in nums if num >> i & 1])
            if cnt >= k:
                res |= 1 << i
        return res


Solution().findKOr1(nums=[10, 8, 5, 9, 11, 6, 8], k=1)
Solution().findKOr1(nums=[7, 12, 9, 8, 9, 15], k=4)
Solution().findKOr1(nums=[2, 12, 1, 11, 4, 5], k=6)
