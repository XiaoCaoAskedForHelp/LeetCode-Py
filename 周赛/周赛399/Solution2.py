class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        start = 0
        end = 1
        while end < len(word):
            if end < len(word) and word[start] == word[end] and end - start + 1 <= 9:
                end += 1
            else:
                comp += str(end - start) + word[start]
                start = end
                end += 1
        comp += str(end - start) + word[start]
        return comp


Solution().compressedString(word="aaaaaaaaaaaaaabb")
Solution().compressedString(word="abcde")
