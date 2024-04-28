class Solution:
    def minEnd(self, n: int, x: int) -> int:
        v = n - 1
        r = x
        k = 0
        while v:
            if (1 << k) & x:
                pass
            else:
                # x这一位为0，就可以拿v中的1进行填充
                if v & 1:
                    r |= (1 << k)
                v >>= 1
            k += 1
        return r

    def minEnd1(self, n: int, x: int) -> int:
        n -= 1
        i = j = 0
        while n >> j:
            # x 的第i个比特位是0
            if (x >> i & 1) == 0:
                # 空位填入n的第j个比特值
                x |= (n >> j & 1) << i
                j += 1
            i += 1
        return x

    # 把x取反，用lowbit枚举其中的1，就是要填的空位
    def minEnd2(self, n: int, x: int) -> int:
        n -= 1
        j = 0
        t = ~x
        while n >> j:
            lb = -t & t  # 去除最低位1
            x |= (n >> j & 1) * lb
            j += 1
            t ^= lb  # 最低位通过异或，清零
        return x


Solution().minEnd2(n=3, x=4)
