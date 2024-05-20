class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dic = {0: -1}
        pre = 0
        ans = 0
        chars = ['a', 'e', 'i', 'o', 'u']  # 只有这些字母需要去算异或前缀和
        for i, c in enumerate(s):
            if c in chars:
                pre ^= 1 << (ord(c) - ord('a'))
            if pre in dic:
                ans = max(ans, i - dic[pre])
            else:
                dic[pre] = i
        return ans
