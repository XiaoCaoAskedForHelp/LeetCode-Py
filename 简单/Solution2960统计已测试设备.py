from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        cnt = 0
        for battery in batteryPercentages:
            if battery - cnt > 0:
                cnt += 1
        return cnt
