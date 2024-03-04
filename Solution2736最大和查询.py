from bisect import bisect_left
from typing import List

from sortedcontainers import SortedList


class Solution:
    # 超过时间限制
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        for x, y in queries:
            tmp = -1
            for j in range(len(nums1)):
                # 感觉这边排序之后更快一点
                if nums1[j] >= x and nums2[j] >= y:
                    tmp = max(nums1[j] + nums2[j], tmp)
            res.append(tmp)
        return res

    #
    def maximumSumQueries1(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        # 根据nums1和queries[1]从大到小排序,这样
        sortedNums = sorted(((num1, num2) for num1, num2 in zip(nums1, nums2)), key=lambda p: -p[0])
        # i 是为了回复queries原本的顺序
        sortedQueries = sorted([[i, x, y] for i, (x, y) in enumerate(queries)], key=lambda p: -p[1])

        j = 0  # 记录query现在查询的位置
        for i, x, y in sortedQueries:
            while j < len(sortedNums) and sortedNums[j][0] >= x:
                num1, num2 = sortedNums[j]
                # 第一个已经比较完了，只需要考虑第二个
                if num2 >= y:
                    ans[i] = max(num1 + num2, ans[i])
                j += 1  # 这样写会出现num1相同情况，无法取到最大值，所以要改一个容器存储一下可能下一轮还有用的nums对

        return ans

    # 先考虑一半，在比较另一半，这样写超时
    # 超时的原因是num1和query都已经排序的，当前一个query查询完毕就可以直接跟着查询第二个query，不需要从头去sortedNums中查询
    def maximumSumQueries2(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        # 根据nums1和queries[1]从大到小排序,这样
        sortedNums = sorted(((num1, num2) for num1, num2 in zip(nums1, nums2)), key=lambda p: -p[0])
        # i 是为了回复queries原本的顺序
        sortedQueries = sorted([[i, x, y] for i, (x, y) in enumerate(queries)], key=lambda p: -p[1])

        stack = []  # 单调栈
        for i, x, y in sortedQueries:
            for num1, num2 in sortedNums:
                if num1 >= x:
                    # num1满足要求了，现在只需要两数之和和第二个数字满足要求就行
                    # num1是从大到小排序的，如果两数之和比栈顶大，那说明num2肯定比之前大,那之前的就可以不要了
                    while stack and stack[-1][1] <= num1 + num2:
                        stack.pop()
                    # 从栈底到栈顶，num2递增，num1 + num2递减的单调栈
                    if not stack or stack[-1][0] < num2:
                        stack.append((num2, num1 + num2))
                else:
                    # 提前中断
                    break
            p = bisect_left(stack, (y,))
            if p < len(stack):
                ans[i] = stack[p][1]
        return ans

    # 需要比较num1、num2、num1 + num2，
    # 先比较num1，筛选出num1符合的，然后构成num2递增，num1 + num2递减的单调栈，然后二分查找栈，让num2符合，这样就能让两数之和最大了。
    def maximumSumQueries3(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        # 根据nums1和queries[1]从大到小排序,这样
        sortedNums = sorted(((num1, num2) for num1, num2 in zip(nums1, nums2)), key=lambda p: -p[0])
        # i 是为了回复queries原本的顺序
        sortedQueries = sorted([[i, x, y] for i, (x, y) in enumerate(queries)], key=lambda p: -p[1])

        stack = []  # 单调栈
        j = 0
        for i, x, y in sortedQueries:
            while j < len(sortedNums) and sortedNums[j][0] >= x:
                num1, num2 = sortedNums[j]
                # num1满足要求了，现在只需要两数之和和第二个数字满足要求就行
                # num1是从大到小排序的，如果两数之和比栈顶大，那说明num2肯定比之前大,那之前的就可以不要了
                while stack and stack[-1][1] <= num1 + num2:
                    stack.pop()
                # 从栈底到栈顶，num2递增，num1 + num2递减的单调栈
                if not stack or stack[-1][0] < num2:
                    stack.append((num2, num1 + num2))
                j += 1
            p = bisect_left(stack, (y,))
            if p < len(stack):
                ans[i] = stack[p][1]
        return ans


Solution().maximumSumQueries1(nums1=[4, 3, 1, 2], nums2=[2, 4, 9, 5], queries=[[4, 1], [1, 3], [2, 5]])
