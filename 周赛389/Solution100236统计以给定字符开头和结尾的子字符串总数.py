class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        # n = len(s)
        # dp = [[0] * (n + 1) for _ in range(n + 1)]
        # for i in range(1, n + 1):
        #     for j in range(i, n + 1):
        #         if s[i - 1] == s[j - 1] == c:
        #             dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1, dp[i - 1][j] + 1)
        #         else:
        #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # return dp[-1][-1]

        # 双指针超时
        # n = len(s)
        # cnt = 0
        # for i in range(n):
        #     if s[i] != c:
        #         continue
        #     for j in range(i, n):
        #         if s[j] == c:
        #             cnt += 1
        # return cnt

        # 数学方法
        cnt = 0
        for i in range(len(s)):
            if s[i] == c:
                cnt += 1
        return (1 + cnt) * cnt // 2
