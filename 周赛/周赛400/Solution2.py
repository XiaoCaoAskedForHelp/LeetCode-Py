from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        start = meetings[0][0]
        end = meetings[0][1]
        for s, e in meetings[1:]:
            if s > end + 1:
                days -= (end - start + 1)
                start = s
                end = e
            else:
                end = max(end, e)
        days -= (end - start + 1)
        return days


Solution().countDays(10, [[5, 7], [1, 3], [9, 10]])
