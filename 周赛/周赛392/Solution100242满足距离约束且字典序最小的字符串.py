class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        # 贪心字典序就是要将字符串前面的字母尽可能变为1
        # 1 2 3 4 5 6  ....    24  25
        # 1 2 3 4 5 6 .....    2   1
        idx = 0
        res = list(s)
        while k and idx < len(s):
            if s[idx] == 'a':
                idx += 1
                continue
            tmp = ord(s[idx]) - ord('a')
            cnt = tmp if tmp <= 13 else 26 - tmp
            # 如果是z这种没有足够的次数变为a，那就只能向下减，
            if cnt <= k:
                res[idx] = 'a'
                k -= cnt
            else:
                res[idx] = chr(ord(s[idx]) - k)
                break
            idx += 1
        return ''.join(res)


print(Solution().getSmallestString(s = "zbbz", k = 3))
