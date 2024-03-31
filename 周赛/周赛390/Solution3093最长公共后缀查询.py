from cmath import inf
from typing import List

# 前缀树
class Solution:
    class Trie:
        def __init__(self):
            self.children = [None] * 26
            self.index = inf
            self.length = inf

        def insert(self, word: str, idx: int):
            n = len(word)
            node = self
            if node.length > n:  # 匹配空字符串的最小的长度字符串的长度和下标也得更新
                node.length = n
                node.index = idx
            for ch in word:
                ch = ord(ch) - ord("a")
                if not node.children[ch]:
                    node.children[ch] = Solution.Trie()
                node = node.children[ch]
                if node.length > n:
                    node.length = n
                    node.index = idx

        def searchPrefix(self, word: str):
            node = self
            for ch in word:
                ch = ord(ch) - ord("a")
                if not node.children[ch]:
                    return node
                node = node.children[ch]
            return node

    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Solution.Trie()
        for idx, word in enumerate(wordsContainer):
            word = word[::-1]
            trie.insert(word, idx)
        res = [-1] * len(wordsQuery)
        for idx, word in enumerate(wordsQuery):
            word = word[::-1]
            node = trie.searchPrefix(word)
            res[idx] = node.index
        return res


Solution().stringIndices(wordsContainer=["abcdefgh", "poiuygh", "ghghgh"], wordsQuery=["gh", "acbfgh", "acbfegh"])
