import numpy


class Solution:
    # 超出内存限制
    def minimumPossibleSum(self, n: int, target: int) -> int:
        nums = []
        for i in range(1, target // 2 + 1):
            if len(nums) == n:
                break
            nums.append(i)
        if len(nums) < n:
            for i in range(target, target + n - target // 2):
                nums.append(i)
        return sum(nums) % (10 ** 9 + 7)

    def minimumPossibleSum1(self, n: int, target: int) -> int:
        mod = 10 ** 9 + 7
        m = target // 2
        if n <= m:
            return (n * (n + 1) // 2) % mod
        # return ((1 + m) * m // 2 + ((target + target + n - m - 1) * (n - m) // 2)) % mod
        return ((1 + m) * m // 2 + (n - m) * target + (n - m) * (n - m - 1) // 2) % mod


Solution().minimumPossibleSum1(39636, 49035)
Solution().minimumPossibleSum(13, 50)
Solution().minimumPossibleSum(3, 3)
Solution().minimumPossibleSum(2, 3)
