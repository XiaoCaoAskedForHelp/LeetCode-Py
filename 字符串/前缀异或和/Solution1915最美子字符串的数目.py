from collections import Counter


class Solution:
    # 若有两个不同下标的前缀和相同，则这两个前缀和的异或结果为 0，意味着这段子串的各个字母的个数均为偶数，符合题目要求。
    # 题目还允许有一个字母出现奇数次，这需要我们寻找两个前缀和，其异或结果的二进制数中恰好有一个 1，意味着这段子串的各个字母的个数仅有一个为奇数。
    def wonderfulSubstrings(self, word: str) -> int:
        cnt = [0] * 1024  # 因为只有10个字母，所以最多就是1024种结果
        cnt[0] = 1  # 初始异或前缀和，需将其计入出现次数
        ans = s = 0
        for c in word:
            s ^= 1 << (ord(c) - ord('a'))  # 计入当前前缀和
            ans += cnt[s]  # 所有字母都出现偶数次
            ans += sum(cnt[s ^ (1 << i)] for i in range(10))  # 枚举其中一个字母出现奇数次
            cnt[s] += 1
        return ans

    def wonderfulSubstrings1(self, word: str) -> int:
        dic = {0: 1}  # 统计异或前缀子串的数量,如果前缀和直接是0，那么可以多加1
        pre = 0
        res = 0
        for i, w in enumerate(word):
            pre ^= 1 << (ord(w) - ord('a'))
            if pre in dic:
                res += dic[pre]
                dic[pre] += 1
            else:
                dic[pre] = 1
            for k in range(10):
                if pre ^ (1 << k) in dic:
                    res += dic[pre ^ (1 << k)]
        return res

    def wonderfulSubstrings2(self, word: str) -> int:
        freq = Counter([0])
        mask, ans = 0, 0

        for ch in word:
            idx = ord(ch) - ord('a')
            mask ^= (1 << idx)
            if mask in freq:
                ans += freq[mask]
            for i in range(10):
                mask_pre = mask ^ (1 << i)
                if mask_pre in freq:
                    ans += freq[mask_pre]
            freq[mask] += 1

        return ans


Solution().wonderfulSubstrings(word="aba")
