class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dict = [0 for _ in range(10)]
        right, half = 0, 0
        for s in secret:
            dict[int(s)] += 1
        for i in range(len(guess)):
            if i < len(secret) and secret[i] == guess[i] and dict[int(guess[i])] > 0:
                right += 1
                dict[int(secret[i])] -= 1
            elif i < len(secret) and secret[i] == guess[i] and dict[int(guess[i])] == 0:
                half -= 1
                right += 1
            elif dict[int(guess[i])] > 0:
                half += 1
                dict[int(guess[i])] -= 1
        return "{0}A{1}B".format(right, half)

    # 统计secret[i]=guess[i] 的下标个数的同时，在 secret[i]≠guess[i] 时，分别统计 secret 和 guess 的各个字符的出现次数
    # 取其在 secret 和 guess 中的出现次数的最小值想和就是结果
    def getHint1(self, secret: str, guess: str) -> str:
        bulls = 0
        cntS, cntG = [0] * 10, [0] * 10
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                cntS[int(s)] += 1
                cntG[int(g)] += 1
        cows = sum(min(s, g) for s, g in zip(cntS, cntG))
        return f'{bulls}A{cows}B'


# Solution().getHint(secret="1123", guess="0111")
# Solution().getHint(secret="1807", guess="7810")

for s, g in zip("abc", "abcde"):
    print(s, g, '\n')
