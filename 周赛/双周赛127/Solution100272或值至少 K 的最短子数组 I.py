from cmath import inf
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = inf
        for i in range(len(nums)):
            res = 0
            b = [False] * 10
            for j in range(i, len(nums)):
                num = nums[j]
                idx = 0
                while num:
                    if num & 1:
                        if not b[idx]:
                            res += (2 ** idx)
                            b[idx] = True
                    idx += 1
                    num >>= 1
                if res >= k:
                    cnt = min(cnt, j - i + 1)
        return cnt if cnt != inf else -1
