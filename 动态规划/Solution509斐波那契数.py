class Solution:
    def fib(self, n: int) -> int:
        # 排除 Corner Case
        if n == 0:
            return 0

        # 创建 dp table
        dp = [0] * (n + 1)

        # 初始化 dp 数组
        dp[0] = 0
        dp[1] = 1

        # 遍历顺序: 由前向后。因为后面要用到前面的状态
        for i in range(2, n + 1):
            # 确定递归公式/状态转移公式
            dp[i] = dp[i - 1] + dp[i - 2]

        # 返回答案
        return dp[n]

    def fib1(self, n: int) -> int:
        if n <= 1:
            return n

        prev1, prev2 = 0, 1
        for _ in range(2, n + 1):
            curr = prev1 + prev2
            prev1, prev2 = prev2, curr
        return prev2

    def fib2(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0, 1]

        for i in range(2, n + 1):
            total = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = total

        return dp[1]

    def fib3(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib3(n - 1) + self.fib3(n - 2)
