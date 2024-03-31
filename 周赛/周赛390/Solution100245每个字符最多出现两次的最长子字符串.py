import collections
from collections import defaultdict


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        # 双指针滑动窗口
        res = 0
        left = right = 0
        dic = defaultdict(int)
        while right < len(s):
            while right < len(s) and dic[s[right]] <= 1:
                dic[s[right]] += 1
                right += 1
            res = max(res, right - left)
            if right < len(s):
                while s[left] != s[right]:
                    dic[s[left]] -= 1
                    left += 1
            left += 1
            right += 1
        return res

    # 从每一个位置开始枚举，只要不超过2就可以继续向后
    def maximumLengthSubstring1(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n):
            cnt = collections.Counter()
            for j in range(i, n):
                cnt[s[j]] += 1
                if cnt[s[j]] > 2:
                    break
                ans = max(ans, j - i + 1)
        return ans


Solution().maximumLengthSubstring1(s="bcbbbcba")
