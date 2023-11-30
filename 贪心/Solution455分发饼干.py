from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        index = len(s) - 1
        res = 0
        for i in range(len(g) - 1, -1, -1):
            if index >= 0 and s[index] >= g[i]:
                res += 1
                index -= 1
        return res

    def findContentChildren1(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        index = 0
        for i in range(len(s)):
            if index < len(g) and s[i] >= g[index]:
                index += 1
        return index