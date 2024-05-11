from collections import Counter, defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        m, p, g = 0, 0, 0
        cnt = 0
        for i, gar in enumerate(garbage):
            dic = Counter(gar)
            if dic["M"]:
                m = i
            if dic["P"]:
                p = i
            if dic["G"]:
                g = i
            cnt += len(gar)
        sums = list(accumulate(travel, initial=0))
        res = cnt + sums[m] + sums[p] + sums[g]
        return res

    # 先让所有垃圾车都跑满全程，再倒着遍历 garbage，减去多跑的时间。
    def garbageCollection1(self, garbage: List[str], travel: List[int]) -> int:
        ans = sum(map(len, garbage)) + sum(travel) * 3
        for c in "MPG":  # 去找每一种垃圾的最后出现的地方，如果没出现就可以减去travel时间
            for g, t in zip(reversed(garbage), reversed(travel)):
                if c in g:
                    break
                ans -= t  # 没有垃圾c，多跑了
        return ans

    # 所有 garbage[i] 的长度之和，加上 tMap 中保存的没量垃圾车的行驶用时之和。
    def garbageCollection2(self, garbage: List[str], travel: List[int]) -> int:
        ans = sumt = 0
        t_map = {}
        for g, t in zip(garbage, [0] + travel):
            ans += len(g)  # 这个操作确实好，感觉就是看透了本质，因为不管如何len(g)都是需要的
            sumt += t  # 计算到现在这个地方的travel所花费的时间
            for c in g:
                t_map[c] = sumt
        return ans + sum(t_map.values())

    # 进一步地，在遍历garbage的过程中把行驶时间加入答案，从而做到一次遍历。
    def garbageCollection3(self, garbage: List[str], travel: List[int]) -> int:
        ans = sumt = 0
        tmap = defaultdict(int)
        for g, t in zip(garbage, [0] + travel):
            ans += len(g)
            sumt += t
            for c in g:
                ans += sumt - tmap[c]  # 其实也就加了一次，因为后面再出现，相减就为0了，不过这个感觉有点难想，绕了点
                tmap[c] = sumt
        return ans

    # 倒序一次遍历法
    def garbageCollection4(self, garbage: List[str], travel: List[int]) -> int:
        ans = len(garbage[0])  # 因为travel少1，所以zip的时候会少1
        seen = set()  # 从后往前，只要在集合中的都是就是需要计算travel的
        for g, t in zip(reversed(garbage), reversed(travel)):
            seen.update(g)
            ans += len(g) + t * len(seen)
        return ans


Solution().garbageCollection(garbage=["G", "P", "GP", "GG"], travel=[2, 4, 3])
