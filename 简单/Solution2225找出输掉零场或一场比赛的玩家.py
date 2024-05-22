from collections import Counter
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        st1 = set()
        st2 = set()
        st3 = set()
        for w, l in matches:
            if w not in st3 and w not in st2:
                st1.add(w)
            if l not in st3:
                if l in st1:
                    st1.remove(l)
                if l in st2:
                    st2.remove(l)
                    st3.add(l)
                else:
                    st2.add(l)
        return [sorted(list(st1)), sorted(list(st2))]

    def findWinners1(self, matches: List[List[int]]) -> List[List[int]]:
        players = set(x for m in matches for x in m)  # 得到所有的player
        loss_count = Counter(loser for _, loser in matches)  # 所有失败的过的人
        return [sorted(x for x in players if x not in loss_count),
                sorted(x for x, c in loss_count.items() if c == 1)]
