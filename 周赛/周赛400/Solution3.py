import bisect
from collections import Counter, defaultdict


class Solution:
    def clearStars(self, s: str) -> str:
        dic = defaultdict(list)
        for i, c in enumerate(s):
            dic[c].append(i)
        if not dic["*"]:
            return s
        s = list(s)
        for idx in dic['*']:
            s[idx] = ''
            for k in sorted(dic.keys()):
                if k == '*':
                    continue
                index = bisect.bisect_right(dic[k], idx)
                if index == 0:
                    continue
                else:
                    s[dic[k][index - 1]] = ""
                    dic[k].remove(dic[k][index - 1])
                    break

        return str.join("", s)


Solution().clearStars(s="aaba*")
