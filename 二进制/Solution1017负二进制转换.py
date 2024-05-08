class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        ans = ""
        while n != 0:
            if n % (-2) == 0:  # 当n为偶数，当前n的最低位为0
                ans += "0"
            else:  # 当前n为奇数，当前n的最低位f为1
                n -= 1  # 将最低位的值抹去后，使得n变为偶数，在进行除负二操作时是整除
                ans += '1'

            n //= -2
        ans = ans[::-1]
        return ans

    # 由于「负二进制」表示中的每一位都是 0 或 1，因此余数的可能取值是 0 和 1
    # 计算第i位上的数字时，此时ni = ni+1 * x + r,其中r就是这位上的数字，就是余数，x就是进制
    def baseNeg21(self, n: int) -> str:
        if n == 0 or n == 1:
            return str(n)
        res = []
        while n:
            remainder = n & 1
            res.append(str(remainder))
            n -= remainder
            n //= -2  # 因为是-2进制
        return ''.join(res[::-1])

    #  n的「负二进制」数等于 maxVal⊕(maxVal−n)
    def baseNeg22(self, n: int) -> str:
        val = 0x55555555 ^ (0x55555555 - n)
        if val == 0:
            return "0"
        res = []
        while val:
            res.append(str(val & 1))
            val >>= 1
        return ''.join(res[::-1])


Solution().baseNeg2(n=4)
