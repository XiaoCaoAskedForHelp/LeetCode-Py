from cmath import inf
from typing import List


class Solution:

    # 枚举中间的数，然后只需要找出两边的最小值，可以使用前后缀最小值的方式计算，前缀最小值可以和答案一起算
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * n
        suf[-1] = nums[-1]
        for i in range(n - 2, 1, -1):
            suf[i] = min(suf[i + 1], nums[i])

        ans = inf
        pre = nums[0]  # 通过这个来计算前缀最小值
        for j in range(1, n - 1):  # 枚举中间的数
            if pre < nums[j] > suf[j + 1]:  # 山形
                ans = min(ans, pre + nums[j] + suf[j + 1])  # 更新答案
            pre = min(pre, nums[j])
        return ans if ans < inf else -1

    def minimumSum1(self, nums: List[int]) -> int:
        n = len(nums)
        res = inf
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] and nums[j] > nums[k]:
                        res = min(res, nums[i] + nums[j] + nums[k])
        return res if res != inf else -1
