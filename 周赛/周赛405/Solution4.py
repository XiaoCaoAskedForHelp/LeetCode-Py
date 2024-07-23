from math import inf
from typing import List


class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        wordss = []
        costss = []
        for i, w in enumerate(words):
            if w in target:
                wordss.append(w)
                costss.append(costs[i])
        if len(wordss) == 0:
            return -1
        dp = [0] + [inf] * len(target)
        for i in range(1, len(target) + 1):
            for j, w in enumerate(wordss):
                if i >= len(w):
                    if w == target[i - len(w): i]:
                        dp[i] = min(dp[i], dp[i - len(w)] + costss[j])
        return dp[len(target)] if dp[len(target) != inf] else -1


Solution().minimumCost(target="abcdef", words=["abdef", "abc", "d", "def", "ef"], costs=[100, 1, 1, 10, 5])
