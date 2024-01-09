class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 创建一个二维数组 dp，用于存储最长公共子序列的长度
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # 遍历数组 text1
        for i in range(1, len(text1) + 1):
            # 遍历数组 text2
            for j in range(1, len(text2) + 1):
                # 如果 text1[i-1] 和 text2[j-1] 相等
                if text1[i - 1] == text2[j - 1]:
                    # 在当前位置上的最长公共子序列长度为前一个位置上的长度加一
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # 如果不相等
                else:
                    # 在当前位置上的最长公共子序列长度为前一个位置上的长度和上一个位置上的长度的最大值
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # 返回最长公共子序列的长度
        return dp[-1][-1]

    # 一维dp数组
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            pre = 0
            for j in range(1, n + 1):
                tmp = dp[j]
                if text1[i - 1] == text2[j - 1]:
                    dp[j] = pre + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                pre = tmp
        return dp[-1]
