class Solution:

    # 官方题解
    def longestAwesome(self, s: str) -> int:
        n = len(s)
        prefix = {0: -1}  # 最先出现前缀异或和的位置
        ans, sequence = 0, 0

        for j in range(n):
            digit = ord(s[j]) - ord("0")
            sequence ^= (1 << digit)  # 子序列的前缀异或和
            if sequence in prefix:
                ans = max(ans, j - prefix[sequence])
            else:
                prefix[sequence] = j
            for k in range(10):  # 可以有一位不一样
                if sequence ^ (1 << k) in prefix:
                    ans = max(ans, j - prefix[sequence ^ (1 << k)])
        return ans

    # 用一个长为 10 的二进制数 mask 记录一个子串中的每个数字的出现次数的奇偶性，例如 mask=0000001101（从右往左读）表示子串中的数字 0,2,3 出现了奇数次，其余数字出现了偶数次。
    # 定义 s 的异或前缀和 pre[i]，等于 s[0] 到 s[i] 这个子串（前缀）中的每个数字的出现次数的奇偶性。
    # 从 s[i+1] 到 s[j] 的这个长为 j−i 的子串，其中每个数字的出现次数的奇偶性，等于pre[j]⊕pre[i]
    def longestAwesome1(self, s: str) -> int:
        D = 10  # s中的字符种类数
        n = len(s)
        pos = [n] * (1 << D)  # n表示没有找到异或前缀和，最大就是10都是1的情况，所以可能出现1<<D种前缀异或和
        pos[0] = -1
        ans = pre = 0  # pre表示子序列的异或前缀和
        for i, x in enumerate(map(int, s)):
            pre ^= 1 << x  # 此时的前缀异或和
            # 第二个数所有数字都是偶数的情况,第三个数是其中有一个数字出现奇数次的情况
            ans = max(ans, i - pos[pre], max(i - pos[pre ^ (1 << d)] for d in range(D)))
            if pos[pre] == n:  # 首次遇到值为pre的前缀异或和，记录其下标为i
                pos[pre] = i
        return ans


Solution().longestAwesome(s="3242415")
