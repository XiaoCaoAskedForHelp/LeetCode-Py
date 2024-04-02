from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        mod = 1_000_000_007
        nums.sort()

        @cache
        def dp(root: int, length: int):
            cnt = defaultdict(int)
            if length == 2:
                for i in range(root):
                    diff = nums[root] - nums[i]  # 如果长度为2，那么固定了root结果，只需要在选一个数字
                    cnt[diff] += 1
            else:
                for i in range(length - 2, root):  # root前一个数可以取的范围就是长度-2到root之前
                    diff = nums[root] - nums[i]
                    for lastDiff, lastCnt in dp(i, length - 1).items():  # 遍历之前的长度的最小值
                        if lastDiff < diff:   # 和之前的最小插值作比较，如果现在的更小，就将计数加在现在的最小插值上
                            cnt[lastDiff] += lastCnt
                        else:
                            cnt[diff] += lastCnt
            return cnt  # 返回当前长度的最小的插值的奇数

        # 动 态规划状态去描述这个过程，维护状态 dps[i][length] = {diff:cnt} 意为，以下标 i 作为结尾，在 nums 下标 0 到 i 这个区间内，
        # 选出 length 个数字，能出的结果整理为一个字典，diff 是差额，cnt 是对应差额的数量；
        ans = 0
        for i in range(k - 1, len(nums)):
            for diff, cnt in dp(i, k).items():  # 以i为结尾，k为长度
                ans = (ans + diff * cnt) % mod
        return ans
