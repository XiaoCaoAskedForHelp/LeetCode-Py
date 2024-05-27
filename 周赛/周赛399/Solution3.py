from collections import Counter
from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        m = len(nums1)
        n = len(nums2)
        for i in range(n):
            nums2[i] *= k
        res = 0
        nums2.sort()
        nums1.sort()
        for i in nums1:
            for j in nums2:
                if i < j:
                    break
                if i % j == 0:
                    res += 1
        return res

    def numberOfPairs1(self, nums1: List[int], nums2: List[int], k: int) -> int:
        m = len(nums1)
        n = len(nums2)
        for i in range(n):
            nums2[i] *= k
        res = 0
        nums2.sort()
        dic = Counter(nums1)
        mx = max(nums1)
        for j in nums2:
            if j == 1:
                res += m
                continue
            i = 1
            while j * i <= mx:
                if j * i in dic:
                    res += dic[j * i]
                i += 1
        return res


Solution().numberOfPairs1(nums1=[70, 70], nums2=[6, 10], k=7)
Solution().numberOfPairs1(nums1=[1, 3, 4], nums2=[1, 3, 4], k=1)
Solution().numberOfPairs1(nums1=[1, 2, 4, 12], nums2=[2, 4], k=3)
Solution().numberOfPairs1([28, 42], [6, 4], 7)
