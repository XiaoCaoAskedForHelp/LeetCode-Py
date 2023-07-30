class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

    def climbStairs1(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0] * 3
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            total = dp[1] + dp[2]
            dp[1] = dp[2]
            dp[2] = total

        return dp[2]

    def climbStairs2(self, n: int) -> int:
        if n <= 1:
            return n

        prev1 = 1
        prev2 = 2
        for i in range(3, n + 1):
            total = prev1 + prev2
            prev1 = prev2
            prev2 = total

        return prev2
