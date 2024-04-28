from cmath import inf
from collections import Counter
from typing import List


class Solution:
    # 枚举 nums1 中保留的最小元素是nums1[0]还是nums1[1]还是nums1[2]
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        # 倒着枚举是因为nums[i]越大答案越小，第一个满足的就是答案
        for i in range(2, -1, -1):
            diff = nums2[0] - nums1[i]
            # 在{nums1[i] + diff}中找子序列nums2
            j = 0
            for v in nums1[i:]:
                if j < len(nums2) and nums2[j] - v == diff:
                    j += 1
                    # 如果nums2是{nums1[i] + diff}的子序列
                    if j == len(nums2):
                        return diff

    def minimumAddedInteger1(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        n = len(nums1)
        ans = 1000
        for i in range(n):
            for j in range(i):
                a = nums1.copy()
                a.pop(i)
                a.pop(j)
                x = nums2[0] - a[0]
                a = [ai + x for ai in a]
                if a == nums2:
                    ans = min(ans, x)
        return ans

    def minimumAddedInteger2(self, nums1: List[int], nums2: List[int]) -> int:
        for i in range(-1000, 1001):
            cnt = Counter(nums1)
            for x in nums2:
                if cnt[x - i] == 0:
                    break
                cnt[x - i] -= 1
            else:
                return i  # 没有遇到任何break就会执行，i就是最小的差值

    def minimumAddedInteger3(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        n = len(nums1)
        m = len(nums2)
        res = inf
        for i in range(n):
            for j in range(i + 1, n):
                k1 = 0
                d = inf
                l = 0
                for k2 in range(m):
                    while k1 == i or k1 == j:
                        k1 += 1
                    if d == inf:
                        d = nums2[k2] - nums1[k1]
                        if d >= res:
                            break
                    if d == nums2[k2] - nums1[k1]:
                        k1 += 1
                        l += 1
                if l == m:
                    res = min(res, d)
        return res



Solution().minimumAddedInteger3(nums1=[3, 5, 5, 3], nums2=[7, 7])
