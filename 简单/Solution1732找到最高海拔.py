from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxh, altitude = 0, 0
        for g in gain:
            altitude += g
            maxh = max(maxh, altitude)

        return maxh
