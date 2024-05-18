from typing import List


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        m = 0
        res = divisors[0]
        for divisor in divisors:
            cnt = 0
            for num in nums:
                if num % divisor == 0:
                    cnt += 1
            if cnt > m:
                m = cnt
                res = divisor
            elif cnt == m:
                res = min(res, divisor)
        return res

    def maxDivScore1(self, nums: List[int], divisors: List[int]) -> int:
        max_cnt, ans = -1, 0
        for d in divisors:
            cnt = sum(1 for x in nums if x % d == 0)
            if cnt > max_cnt or cnt == max_cnt and d < ans:
                max_cnt, ans = cnt, d
        return ans

    # 把 nums 排序，从大到小遍历 nums。只需遍历 ≥d 的 nums[i]，当 nums[i]<d 时，退出内层循环。

    def maxDivScore2(self, nums: List[int], divisors: List[int]) -> int:
        nums.sort(reverse=True)
        max_cnt, ans = -1, 0
        for d in divisors:
            cnt = 0
            for x in nums:
                if x < d:
                    break
                if x % d == 0:
                    cnt += 1
            if cnt > max_cnt or cnt == max_cnt and d < ans:
                max_cnt, ans = cnt, d
        return ans

    # (maxCnt−dup+1)⋅d>max(nums)   说明 d 的倍数 d,2d,3d,⋯,(maxCnt−dup+1)⋅d 中的最大值已经超出了 nums 的最大值
    # 即使把 nums 中的重复元素也算上，我们也无法统计出比 maxCnt 还多的倍数，所以直接退出外层循环
    import itertools
    def maxDivScore3(self, nums: List[int], divisors: List[int]) -> int:
        nums.sort(reverse=True)
        pre = -1
        dup = 0
        for num in nums:
            if num == pre:
                dup += 1
            else:
                pre = num
        divisors.sort()
        max_cnt, ans = -1, 0
        for d in divisors:
            if (max_cnt - dup + 1) * d > nums[0]:
                break
            cnt = 0
            for x in nums:
                if x < d:
                    break
                if x % d == 0:
                    cnt += 1
            if cnt > max_cnt:
                max_cnt, ans = cnt, d
        return ans


Solution().maxDivScore3(nums = [20,14,21,10], divisors = [5,7,5])
