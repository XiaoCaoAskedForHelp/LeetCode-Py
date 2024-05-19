from collections import defaultdict
from typing import List


class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        m = len(str(nums[0]))
        total = n * (n - 1) // 2  # 全部都不同
        res = 0
        for i in range(m):
            dic = defaultdict(int)
            for j in range(n):
                dic[str(nums[j])[i]] += 1
            tmp = 0
            for v in dic.values():
                if v > 1:
                    tmp += v * (v - 1) // 2
            res += total - tmp
        return res


print(Solution().sumDigitDifferences(nums=[50, 28, 48]))
print(Solution().sumDigitDifferences(nums=[13, 23, 12]))
print(Solution().sumDigitDifferences(nums=[10, 10, 10, 10]))
