class Solution:
    # dp
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        # dp[i][j] 表示s[i,j] 是否是回文子串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        max_len = 1  # 回文串的长度
        max_str = s[0]  # 回文串
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                # 如果长度为2
                if j - i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]

                if dp[i][j] and j - i + 1 > max_len:
                    max_str = s[i:j + 1]
                    max_len = j - i + 1
        return max_str

    # 从已知的left，right向外扩张
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    # Manacher 算法
    def longestPalindrome1(self, s: str) -> str:
        start, end = 0, -1
        s = '#' + '#'.join(list(s)) + '#'
        arm_len = []  # 存储每一个的点的臂长
        right = -1
        j = -1
        for i in range(len(s)):
            if right >= i:
                i_sym = 2 * j - i  # 找到对称点
                min_arm_len = min(arm_len[i_sym], right - i)  # 能确定下来的臂长就是对称点的臂长和最右侧点到i的长度这两者的最小值
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:
                cur_arm_len = self.expand(s, i, i)  # 如果right还没有覆盖这个点，那么就只能从中心点扩张
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > right:
                j = i  # 更新中心点
                right = i + cur_arm_len  # 更新能达到的最右点
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len  # 更新最长回文串的左右下标
        return s[start + 1: end + 1:2]


Solution().longestPalindrome1("aaaa")
