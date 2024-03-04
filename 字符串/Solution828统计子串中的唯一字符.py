import collections


class Solution:
    # 超时
    def uniqueLetterString(self, s: str) -> int:
        def is_unique(start: int, end: int) -> int:
            cnt = 0
            for i in range(start, end):
                if s[end] == s[i]:
                    cnt += 1
            if cnt > 1:
                return 0
            elif cnt == 1:
                return -1
            else:
                return 1

        n = len(s)
        dp = [[0] * n for _ in range(n)]  # 下标从i到j子字符串的唯一字符
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j - 1] + is_unique(i, j)

        cnt = 0
        for i in range(n):
            for j in range(i, n):
                cnt += dp[i][j]

        return cnt

    def uniqueLetterString1(self, s: str) -> int:
        def is_unique(dict: [], ch) -> int:
            if dict[ord(ch) - ord('A')] > 1:
                return 0
            elif dict[ord(ch) - ord('A')] == 1:
                return -1
            else:
                return 1

        n = len(s)
        dp = [[0] * n for _ in range(n)]  # 下标从i到j子字符串的唯一字符
        res = 0
        for i in range(n - 1, -1, -1):
            dict = [0] * 26
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                    dict[ord(s[i]) - ord('A')] += 1
                else:
                    dp[i][j] = dp[i][j - 1] + is_unique(dict, s[j])
                    dict[ord(s[j]) - ord('A')] += 1
                res += dp[i][j]

        return res

    # 当它在某个子字符串中仅出现一次时，它会对这个子字符串统计唯一字符时有贡献
    # 如何统计一个字符在一个子字符串中只出现一次呢，那就是上一个出现位置到这一个出现位置*这一个出现位置到下一个出现位置
    def uniqueLetterString2(self, s: str) -> int:
        index = collections.defaultdict(list)
        for i, c in enumerate(s):
            index[c].append(i)

        res = 0
        for arr in index.values():
            arr = [-1] + arr + [len(s)]
            for i in range(1, len(arr) - 1):
                res += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
        return res


Solution().uniqueLetterString("ABC")
Solution().uniqueLetterString("ABA")
Solution().uniqueLetterString("LEETCODE")
