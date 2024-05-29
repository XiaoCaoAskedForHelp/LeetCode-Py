from collections import defaultdict


class Solution:
    # "eccdnmcnkl"无法解决这种字符串问题,需要详细解决一下
    def maximumLength(self, s: str) -> int:
        dic = defaultdict(int)
        start = end = 0
        mlen = 0
        while end < len(s):
            while end + 1 < len(s) and s[end + 1] == s[start]:
                end += 1
                continue
            l = end - start + 1
            for i in range(start, end + 1):
                dic[s[start:i + 1]] += end - i + 1
            mlen = max(l, mlen)
            start = end = end + 1
        res = 0
        for k, v in dic.items():
            if v >= 3:
                res = max(res, len(k))
        return max(res, mlen - 2) if max(res, mlen - 2) != 0 else -1

    # 字符串 aaaabbbabb 分成 aaaa+bbb+a+bb 四组
    # 字母 a 的长度列表为 [4,1]，字母 b 的长度列表为 [3,2]
    # 取出三个特殊子串的方法
    # 从最长的特殊子串（a[0]）中取三个长度均为 a[0]−2 的特殊子串。例如示例 1 的 aaaa 可以取三个 aa。
    # 从最长和次长的特殊子串（a[0],a[1]）中取三个长度一样的特殊子串
    #   如果 a[0]=a[1]，那么可以取三个长度均为 a[0]−1 的特殊子串。
    #   如果 a[0]>a[1]，那么可以取三个长度均为 a[1] 的特殊子串：从最长中取两个，从次长中取一个。
    # 这两种情况合并成 min(a[0]−1,a[1])。
    # 最长、次长、第三长的的特殊子串（a[0],a[1],a[2]）中各取一个长为 a[2] 的特殊子串。
    # 三种情况取最大值max(a[0]−2,min(a[0]−1,a[1]),a[2])
    def maximumLength1(self, s: str) -> int:
        groups = defaultdict(list)
        cnt = 0
        for i, ch in enumerate(s):
            cnt += 1
            if i + 1 == len(s) or ch != s[i + 1]:
                groups[ch].append(cnt)  # 统计连续字符长度
                cnt = 0
        ans = 0
        for a in groups.values():
            a.sort(reverse=True)
            a.extend([0, 0])  # 假设还有两个空串，因为计算的时候最多用到前三个字符串，加上这两个0可以防止取值异常
            ans = max(ans, a[0] - 2, min(a[0] - 1, a[1]), a[2])
        return ans if ans else -1
