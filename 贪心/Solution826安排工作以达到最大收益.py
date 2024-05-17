from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        task = sorted(zip(difficulty, profit), key=lambda x: x[0])
        maxp = 0
        idx = 0
        res = 0
        worker.sort()
        for w in worker:
            while idx < len(task) and task[idx][0] <= w:
                maxp = max(maxp, task[idx][1])
                maxp = max(maxp, task[idx][1])
                idx += 1
            res += maxp
        return res


Solution().maxProfitAssignment(difficulty=[13, 37, 58], profit=[4, 90, 96], worker=[34, 73, 45])
