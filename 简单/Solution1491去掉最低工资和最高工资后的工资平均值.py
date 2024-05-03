from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return sum(sorted(salary)[1:-1]) / (len(salary) - 2)

    def average1(self, salary: List[int]) -> float:
        s = sum(salary)
        m = min(salary)
        M = max(salary)
        n = len(salary)
        return (s - m - M) / (n - 2)
