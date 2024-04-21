class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cnt = 0
        st1 = [-1] * 26  # 大写的最前的位置
        st2 = [-1] * 26  # 小写字母最后的位置
        for i in range(len(word)):
            ch = word[i]
            if ord('A') <= ord(ch) <= ord('Z'):
                tmp = ord(ch) - ord('A')
                if st1[tmp] == -1:
                    st1[tmp] = i
            elif ord('a') <= ord(ch) <= ord('z'):
                tmp = ord(ch) - ord('a')
                st2[tmp] = i
        for i in range(26):
            if st1[i] != -1 and st2[i] != -1 and st2[i] < st1[i]:
                cnt += 1
        return cnt


Solution().numberOfSpecialChars(word="AbBCab")
