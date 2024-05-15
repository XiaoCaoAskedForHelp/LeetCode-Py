from typing import List


class Solution:
    # 每个节点维护对应区间的
    # 前缀最长连续字符个数pre
    # 后缀最长连续字符个数suf
    # 区间最长连续字符个数max
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        s = list(s)
        pre = [0] * (n * 4)
        suf = [0] * (n * 4)
        mx = [0] * (n * 4)

        # 最主要的函数，如何进行区间合并
        def pushup(o: int, l: int, r: int):
            pre[o] = pre[o * 2]
            suf[o] = suf[o * 2 + 1]
            mx[o] = max(mx[o * 2], mx[o * 2 + 1])
            m = (l + r) // 2
            if s[m - 1] == s[m]:  # 中间字符相同，也就是o * 2和o * 2 + 1这两个区间的两段左右端点相同，m和m-1是因为s的下标和线段树下标差1
                if suf[o * 2] == m - l + 1:  # 如果o * 2的前缀字符长度都相同等于区间长度时，可以连上后一段区间的前缀
                    pre[o] += pre[o * 2 + 1]
                if pre[o * 2 + 1] == r - m:
                    suf[o] += suf[o * 2]
                mx[o] = max(mx[o], suf[o * 2] + pre[o * 2 + 1])  # 最大值可能变为前一段区间的后缀 + 后一段区间的前缀

        def build(o: int, l: int, r: int):
            if l == r:
                pre[o] = suf[o] = mx[o] = 1
                return
            m = (l + r) // 2
            build(o * 2, l, m)
            build(o * 2 + 1, m + 1, r)
            pushup(o, l, r)

        def update(o: int, l: int, r: int, i: int):
            if l == r:
                return
            m = (l + r) // 2
            if i <= m:  # 只影响一边
                update(o * 2, l, m, i)
            else:
                update(o * 2 + 1, m + 1, r, i)
            pushup(o, l, r)

        build(1, 1, n)
        ans = []
        for c, i in zip(queryCharacters, queryIndices):
            s[i] = c
            update(1, 1, n, i + 1)
            ans.append(mx[1])
        return ans
