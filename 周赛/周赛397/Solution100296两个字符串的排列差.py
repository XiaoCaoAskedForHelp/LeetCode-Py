class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        res = 0
        for i, num in enumerate(s):
            j = t.index(num)
            res += abs(i - j)
        return res


Solution().findPermutationDifference(s="abcde", t="edbac")
