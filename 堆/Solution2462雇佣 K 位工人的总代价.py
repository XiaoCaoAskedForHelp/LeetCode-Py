import heapq
from typing import List


class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if candidates * 2 >= n:
            return sum(sorted(costs)[:k])
        left, right = candidates, n - 1 - candidates
        queue = []
        for i in range(candidates):
            heapq.heappush(queue, (costs[i], i))
        for i in range(n - candidates, n):
            heapq.heappush(queue, (costs[i], i))
        res = 0
        while k:
            c, idx = heapq.heappop(queue)
            res += c
            if left <= right:
                if idx < left:
                    heapq.heappush(queue, (costs[left], left))
                    left += 1
                else:
                    heapq.heappush(queue, (costs[right], right))
                    right -= 1
            k -= 1
        return res

    # 用两个最小堆来模拟，一个负责维护 costs 剩余数字的最前面 candidates 个数的最小值，另一个负责维护 costs 剩余数字的最后面 candidates个数的最小值
    def totalCost1(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if candidates * 2 + k > n:  # 一定可以选到 cost 中最小的 k 个数
            costs.sort()
            return sum(costs[:k])
        pre = costs[:candidates]  # 最前面 candidates 个数的最小值
        suf = costs[-candidates:]  # 维护 costs 剩余数字的最后面 candidates个数的最小值
        heapq.heapify(pre)
        heapq.heapify(suf)

        ans = 0
        i = candidates
        j = n - 1 - candidates
        for _ in range(k):
            if pre[0] <= suf[0]:  # 选出来小的，并且pre堆中的序号肯定比suf中的序号小
                ans += heapq.heapreplace(pre, costs[i])
                i += 1
            else:
                ans += heapq.heapreplace(suf, costs[j])  # 小的后candidates个数中
                j -= 1
        return ans


Solution().totalCost(costs=[17, 12, 10, 2, 7, 2, 11, 20, 8], k=3, candidates=4)
