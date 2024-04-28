import bisect
from collections import Counter
from typing import List


class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        k = (n * (n + 1) // 2 + 1) // 2  # 中位数的位置

        # 子数组的个数为cnt
        def check(upper: int) -> bool:
            cnt = l = 0
            freq = Counter()
            for r, in_ in enumerate(nums):
                freq[in_] += 1
                while len(freq) > upper:
                    out = nums[l]
                    freq[out] -= 1
                    if freq[out] == 0:
                        del freq[out]
                    l += 1
                cnt += r - l + 1  # 右边点固定为r，左端点从l到r到子序列都满足条件
                if cnt >= k:
                    return True
            return False

        return bisect.bisect_left(range(len(set(nums))), True, 1, key=check)  # 要查找的目标值，搜索的其实位置
