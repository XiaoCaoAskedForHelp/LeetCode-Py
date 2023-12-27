from typing import List


class Solution:
    # 单纯的回溯超时了，需要加上记忆模块
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # 转换为哈希集合，提高查找效率
        return self.backtracking(s, wordSet, 0)

    def backtracking(self, s: str, wordSet: set[str], startIndex: int) -> bool:
        # 边界情况：已经遍历到字符串末尾，返回True
        if startIndex >= len(s):
            return True
        # 遍历所有可能的拆分位置
        for i in range(startIndex, len(s)):
            word = s[startIndex:i + 1]  # 截取子串
            if word in wordSet and self.backtracking(s, wordSet, i + 1):
                # 如果截取的子串在字典中，并且后续部分也可以被拆分成单词，返回True
                return True

        # 无法进行有效拆分，返回False
        return False

        # 单纯的回溯超时了，需要加上记忆模块

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo = [0] * len(s)
        wordSet = set(wordDict)  # 转换为哈希集合，提高查找效率
        return self.backtracking(s, wordSet, 0)

    def backtracking(self, s: str, wordSet: set[str], startIndex: int) -> bool:
        # 边界情况：已经遍历到字符串末尾，返回True
        if startIndex >= len(s):
            return True
        if self.memo[startIndex] == -1:
            return False
        # 遍历所有可能的拆分位置
        for i in range(startIndex, len(s)):
            word = s[startIndex:i + 1]  # 截取子串
            # 如果截取的子串在字典中，并且后续部分也可以被拆分成单词，返回True
            if not word in wordSet:
                continue
            res = self.backtracking(s, wordSet, i + 1)
            if res:
                return True;

        # 这里是关键，找遍了startIndex~s.length()也没能完全匹配，标记从startIndex开始不能找到
        self.memo[startIndex] = -1
        # 无法进行有效拆分，返回False
        return False

    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)  # dp[i] 表示字符串的前 i 个字符是否可以被拆分成单词
        dp[0] = True  # 初始状态，空字符串可以被拆分成单词

        for i in range(1, n + 1):  # 遍历背包
            for j in range(i):  # 遍历单词
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True  # 如果 s[0:j] 可以被拆分成单词，并且 s[j:i] 在单词集合中存在，则 s[0:i] 可以被拆分成单词
                    break

        return dp[n]

    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)  # dp[i] 表示字符串的前 i 个字符是否可以被拆分成单词
        dp[0] = True  # 初始状态，空字符串可以被拆分成单词

        for i in range(1, n + 1):  # 遍历背包
            for j in range(i):  # 遍历单词
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True  # 如果 s[0:j] 可以被拆分成单词，并且 s[j:i] 在单词集合中存在，则 s[0:i] 可以被拆分成单词
                    break

        return dp[n]

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        # 遍历背包
        for j in range(1, len(s) + 1):
            # 遍历单词
            for word in wordDict:
                if j >= len(word):
                    dp[j] = dp[j] or (dp[j - len(word)] and word == s[j - len(word):j])
        return dp[len(s)]
