class Solution:
    # 统计所有的0，在1后面的所有0 都能被移到前面,然后变为1，最后只剩一个0,但是开头的1不需要动，已经是最大的了
    def maximumBinaryString(self, binary: str) -> str:
        flag = True
        res = []
        cnt0 = 0
        cnt1 = 0
        cnt = 0
        for i in binary:
            if flag:
                if i == "1":
                    res.append("1")
                    cnt += 1
                else:
                    flag = False
            if not flag:
                if i == "1":
                    cnt1 += 1
                else:
                    cnt0 += 1
        res += (['1' for _ in range(cnt0 - 1)] + (['0'] if cnt + cnt1 != len(binary) else []) + ['1' for i in
                                                                                                 range(cnt1)])
        return "".join(res)

    # 只要还有两个 0，那么用操作 2 把右边的 0 往左移，当出现 00 时就通过操作 1 把左边的 0 变成 1，这会让二进制更大。
    def maximumBinaryString1(self, binary: str) -> str:
        i = binary.find("0")
        if i < 0:
            return binary
        cnt1 = binary.count("1", i)  # 统计binary[i:]中1的个数
        return '1' * (len(binary) - 1 - cnt1) + '0' + '1' * cnt1
