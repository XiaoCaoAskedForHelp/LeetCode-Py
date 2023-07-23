from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                if nums2[stack[-1]] in nums1:
                    index = nums1.index(nums2[stack[-1]])
                    result[index] = nums2[i]
                stack.pop()
            stack.append(i)

        return result