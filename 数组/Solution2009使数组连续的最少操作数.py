from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        nums.sort()
        # 计算出最长的连续序列 枚举每一个数字，看在他本身加序列长度范围内的有几个数字，滑动窗口的思想
        cnt = 0
        res = 0  # 不需要改变的最长序列长度
        same = 0
        end = 0
        for i in range(n):
            j = end
            if n - i < res:
                break
            if i != 0 and nums[i] == nums[i - 1]:
                same -= 1
            while j < n and nums[j] < nums[i] + n:
                if nums[j] == nums[j - 1]:
                    same += 1
                j += 1
            end = j
            cnt = j - i - same
            res = max(res, cnt)

        return n - res

    # 设 a 为 nums 排序去重后的数组。把 a[i] 画在一条数轴上，本题相当于有一个长度为 n 的滑动窗口，我们需要计算窗口内最多可以包含多少个数轴上的点。
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        a = sorted(set(nums))  # 去重排序
        ans = left = 0
        # 固定右端点，比较左端点，看能包含多少个数字
        for i, x in enumerate(a):  # a往后遍历，因为a数组是顺序的，所以a后一个比前一个大，left也只会大于等于前一个left
            while a[left] < x - n + 1:  # a[left] 不在窗口内
                left += 1
            ans = max(ans, i - left + 1)
        return n - ans


Solution().minOperations([8, 10, 16, 18, 10, 10, 16, 13, 13, 16])
