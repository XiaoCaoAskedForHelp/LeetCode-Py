class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        st = set()
        word = sorted(word)
        cnt = 0
        for ch in word:
            if ord('A') <= ord(ch) <= ord('Z'):
                st.add(ord(ch))
            if ord('a') <= ord(ch) <= ord('z'):
                if ord(ch) - 32 in st:
                    st.remove(ord(ch) - 32)
                    cnt += 1
        return cnt


Solution().numberOfSpecialChars(word="abBCab")
