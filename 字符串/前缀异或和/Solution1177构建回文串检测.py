from typing import List


class Solution:
    # 比较特殊的地方就是可以有k个数字可以替换，那就说明可以容许2*k + 1个奇数个数字，或是时候[n//2] <= k 就能满足要求
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        count = [0] * (n + 1)
        for i in range(n):
            count[i + 1] = count[i] ^ (1 << (ord(s[i]) - ord('a')))
        res = []
        for l, r, k in queries:
            bits = (count[r + 1] ^ count[l]).bit_count()
            res.append(bits <= k * 2 + 1)
        return res

    # 灵茶山艾府（原始版本）
    def canMakePaliQueries1(self, s: str, queries: List[List[int]]) -> List[bool]:
        sum = [[0] * 26]  # 因为有26个英文字母，需要统计每个字母在子串中的出现次数
        for c in s:
            sum.append(sum[-1].copy())
            sum[-1][ord(c) - ord('a')] += 1
        ans = []
        for l, r, k in queries:
            m = 0
            for sl, sr in zip(sum[l], sum[r + 1]):
                m += (sr - sl) % 2  # 奇数加1 偶数加0
            ans.append(m // 2 <= k)
        return ans

    # 优化版本
    def canMakePaliQueries2(self, s: str, queries: List[List[int]]) -> List[bool]:
        sum = [0]
        for c in s:
            bit = 1 << (ord(c) - ord('a'))
            sum.append(sum[-1] ^ bit)  # 直接拿sum[i]表示0-i这个子串的异或前缀和，其中2^k位上为0，代表这个数字有奇数个
        ans = []
        for l, r, k in queries:
            m = (sum[l] ^ sum[r + 1]).bit_count()  # 直接算出从l到r这个子序列奇数个数字的个数
            ans.append(m // 2 <= k)
        return ans
