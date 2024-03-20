class Solution:
    # 感觉就是要让1变的越多越好，大的数尽可能大，小的数尽可能小
    # 每个位置1的数量都是2的n-1次方，p位数就有2的p次方减一个数，让一个数所有位都是1，其他数一般只有最后一位是1和最后一位不是1
    def minNonZeroProduct(self, p: int) -> int:
        mod = 10 ** 9 + 7
        res = (1 << p) - 1
        m = ((1 << p) - 2) % mod
        # 超时
        # for _ in range(((1 << p) - 2) // 2):
        #     res = (res * m) % mod
        # return res
        pw = ((1 << p) - 2) // 2
        # 快速幂 算m的pw次方
        ans = 1
        while pw:
            if pw | 1:
                ans = (ans * m) % mod
            m = (m * m) % mod
            pw >>= 1
        return (res * ans) % mod

    # 两个数在进行相同的位交换时，本质即将一个元素缩小 2^k，另外一个元素增加 2^k。根据上述分析，我们可以知道一种贪心思路：进行相同位交换时，优先缩小数组中最小的元素，再增加数组中最大的元素。
    def minNonZeroProduct1(self, p: int) -> int:
        if p == 1:
            return 1
        mod = 10 ** 9 + 7
        return pow(2 ** p - 2, 2 ** (p - 1) - 1, mod) * (2 ** p - 1) % mod


Solution().minNonZeroProduct(3)
