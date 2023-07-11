class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # 使用find函数
        if len(s) <= 1:
            return False
        ss = s[1:] + s[:-1]
        return ss.find(s) != -1

    # KMP前缀表
    def repeatedSubstringPattern1(self, s: str) -> bool:
        if len(s) == 0:
            return False;
        next = [0] * len(s)
        self.getNext(next, s)
        if next[-1] != 0 and len(s) % (len(s) - next[-1]) == 0:
            return True
        return False

    def getNext(self, next: list, s: str):
        next[0] = 0
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j

    def repeatedSubstringPattern2(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return False

        substr = ""
        for i in range(1, n // 2 + 1):
            if n % i == 0:
               substr = s[:i]
               if substr * (n//i) == s:
                   return True
        return False