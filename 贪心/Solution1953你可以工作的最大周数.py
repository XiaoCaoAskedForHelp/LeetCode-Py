import heapq
from typing import List


class Solution:
    # 有问题，应该是少考虑的空隙等等
    def numberOfWeeks(self, milestones: List[int]) -> int:
        if len(milestones) == 1:
            return 1
        milestones = [(-task, i) for i, task in enumerate(milestones)]
        heapq.heapify(milestones)
        task, i = heapq.heappop(milestones)
        task = -task
        res = 0
        while milestones:
            next, nexti = heapq.heappop(milestones)
            next = -next
            task -= next
            res += next * 2
            if milestones:
                if task >= -milestones[0][0]:
                    continue
                else:
                    if task != 0:
                        heapq.heappush(milestones, (-task, i))
                    task, i = heapq.heappop(milestones)
                    task = -task
        if task != 0:
            res += 1
        return res

    def numberOfWeeks1(self, milestones: List[int]) -> int:
        # 耗时最长的工作所需的周数
        longest = max(milestones)
        # 其余所有的工作共所需的周数
        rest = sum(milestones) - longest
        if longest > rest + 1:
            # 此时无法完成所耗时最长的工作
            return rest * 2 + 1
        else:
            # 此时可以完成所有工作
            return longest + rest  # 按照从小到大的顺序分配所有的奇数，然后按照从小到大的顺序分配所有的偶数。

    # https://leetcode.cn/problems/maximum-number-of-weeks-for-which-you-can-work/solutions/909585/ezi-zai-fei-hua-e-bi-jiao-hao-li-jie-de-8in32
    # 这个解释的挺清楚的

    def numberOfWeeks2(self, milestones: List[int]) -> int:
        s = sum(milestones)
        m = max(milestones)
        return (s - m) * 2 + 1 if m > s - m + 1 else s


Solution().numberOfWeeks(milestones=[5, 7, 5, 7, 9, 7])
Solution().numberOfWeeks(milestones=[5, 9, 4, 4, 8, 9, 9, 8, 7, 3])
Solution().numberOfWeeks(milestones=[5, 2, 1])
Solution().numberOfWeeks(milestones=[1, 2, 3])
