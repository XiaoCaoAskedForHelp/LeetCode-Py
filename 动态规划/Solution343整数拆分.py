class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[2] = 1

        for i in range(3, n + 1):
            # 遍历所有可能的切割点
            for j in range(1, i // 2 + 1):
                # 计算切割点j和剩余部分(i-j)的乘积，并与之前的结果进行比较取较大值
                dp[i] = max(dp[i], max(j * (i - j), dp[i - j] * j));
        return dp[-1]