from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = mean * (m + n)
        s = sum(rolls)
        left = total - s
        avg = left // n
        if left < n or left > 6 * n:
            return []
        remain = left % n
        return [avg] * (n - remain) + [avg + 1] * remain

    def missingRolls1(self, rolls: List[int], mean: int, n: int) -> List[int]:
        rem = mean * (n + len(rolls)) - sum(rolls)
        if not n <= rem <= n * 6:
            return []
        avg, extra = divmod(rem, n)
        return [avg + 1] * extra + [avg] * (n - extra)
