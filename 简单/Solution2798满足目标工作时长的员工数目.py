from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        cnt = 0
        for i in hours:
            if i >= target:
                cnt += 1
        return cnt

    def numberOfEmployeesWhoMetTarget1(self, hours: List[int], target: int) -> int:
        return sum(h >= target for h in hours)