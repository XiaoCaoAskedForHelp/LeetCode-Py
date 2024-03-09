import heapq
from typing import List

from sortedcontainers import SortedList


class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        totol = 0
        for i in range(n):
            if nums[i] >= 0:
                totol += nums[i]  # 算出所有正数的和
            else:
                nums[i] = -nums[i]  # 将所有负数变为正数，和正数一样处理
        nums = sorted(nums)  # 将序列从小到大排序

        # 接下来就是要求所有这些升序的非负整数的前k个最小和序列
        # 初始化，最小的序列就是空序列
        queue = [(0, -1)]  # 或者这边直接初始化为[(nums[0],0)]最小的数字
        # 需要取出第k个序列最小和，那就说明需要取队头k次,但做操作的只需要k-1次，最后一次直接看队头
        # 每次操作的已有元素序列中最后一个和新的一个元素(为什么不操作序列中的其他元素，已有序列的其他元素之前循环中已经被操作过了)
        for _ in range(k - 1):
            t, i = heapq.heappop(queue)
            if i == n - 1:  # 到最后一个元素了没法操作了
                continue
            # 构成新序列可以有两种操作
            # 第一种就是将序列的元素进行替换
            if i != -1:  # 第一次是空序列不能做操作
                heapq.heappush(queue, (t - nums[i] + nums[i + 1], i + 1))
            # 第二种是在现有序列之后添加一个元素
            heapq.heappush(queue, (t + nums[i + 1], i + 1))

        return totol - queue[0][0]  # 结果就是所有正数的和 - 最小序列和（第k最小序列和） = 剩下需要的大的正数和需要减去的小的负数

    # 二分查找的方式
    def kSum1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        total, total2 = 0, 0  # total记录原nums中所有正数的和，total2记录序列变为非负序列后的和
        for i in range(n):
            if nums[i] >= 0:
                total += nums[i]
            else:
                nums[i] = -nums[i]
            total2 += nums[i]
        nums.sort()  # nums需要变为从小到大有序的

        cnt = 0

        def dfs(i: int, t: int, mid: int):  # mid中间的限制（看到mid这个范围有多少最小序列和） t：序列和   i：遍历的nums中的下标（选或者不选）
            nonlocal cnt
            if i == n or cnt >= k - 1 or t + nums[i] > mid:  # 只要能找到k-1个最小和子序列或者已有序列加上要选择的这个数字就返回
                return
            cnt += 1  # 满足条件就可以计数
            dfs(i + 1, t + nums[i], mid)  # 子序列选i下标这个数字
            dfs(i + 1, t, mid)  # 子序列不选i+1下标这个数字

        left, right = 0, total2
        while left <= right:
            mid = (left + right) // 2
            cnt = 0  # 每一次二分查找都得将cnt置为0
            dfs(0, 0, mid)
            if cnt >= k - 1:  # 为什么是k-1 呢，还要去掉空子序列
                right = mid - 1
            else:
                left = mid + 1

        return total - left


Solution().kSum(nums=[2, 4, -2], k=5)
