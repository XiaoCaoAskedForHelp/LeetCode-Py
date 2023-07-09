class Solution(object):
    def getNext(self, next: list[int], s: str):
        j = 0
        next[0] = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j

    # KMP算法
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        next = [0] * len(needle)
        self.getNext(next, needle)
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1

    # 使用index、find函数
    def strStr1(self, haystack, needle):
        try:
            return haystack.index(needle)
        except:
            return -1

    def strStr2(self, haystack, needle):
        return haystack.find(needle)

    # 暴力解法
    def strStr3(self, haystack, needle):
        m, n = len(haystack), len(needle)
        for i in range(m):
            if haystack[i:i+n] == needle:
                return i
        return -1

Solution().strStr3("sadbutsad", "sad")

print(list(range(10)))
