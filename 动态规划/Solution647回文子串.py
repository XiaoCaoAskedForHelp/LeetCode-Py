class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        res = 0
        for j in range(len(s)):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1
        return res

    def countSubstrings1(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        result = 0
        for i in range(len(s) - 1, -1, -1):  # 注意遍历顺序
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:  # 情况一 和 情况二
                        result += 1
                        dp[i][j] = True
                    elif dp[i + 1][j - 1]:  # 情况三
                        result += 1
                        dp[i][j] = True
        return result

    def countSubstrings2(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.extend(s, i, i, len(s))
            res += self.extend(s, i, i + 1, len(s))
        return res

    def extend(self, s, i, j, n):
        res = 0
        while i >= 0 and j < n and s[i] == s[j]:
            res += 1
            i -= 1
            j += 1
        return res
