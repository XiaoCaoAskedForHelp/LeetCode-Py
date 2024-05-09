from cmath import inf
from typing import List


class Solution:
    # 两人都走一遍，然后去计算最小值，本来以为是每个位置都能作为两人的分界点，结果没想到就是中间作为两人的分界点
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        if len(plants) == 1 or len(plants) == 2:
            return 0
        rea, reb = [], []
        tmp = 0
        water = capacityA
        for plant in plants:
            if water < plant:
                tmp += 1
                water = capacityA
            rea.append(tmp)
            water -= plant

        tmp = 0
        water = capacityB
        for plant in plants[::-1]:
            if water < plant:
                tmp += 1
                water = capacityB
            reb.append(tmp)
            water -= plant
        reb.reverse()

        res = inf
        # for i in range(len(plants) - 1):
        #     res = min(res, rea[i] + reb[i + 1])
        n = len(plants)
        res = rea[n // 2 - 1] + reb[n // 2] if n % 2 == 0 else min(rea[n // 2 - 1] + reb[n // 2],
                                                                   rea[n // 2] + reb[n // 2 + 1])
        return res

    def minimumRefill1(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        ans = 0
        a, b = capacityA, capacityB
        i, j = 0, len(plants) - 1
        while i < j:
            # Alice 给植物i浇水
            if a < plants[i]:
                # 没有足够的水,返回起点重新装满水罐
                ans += 1
                a = capacityA
            a -= plants[i]
            i += 1
            # Bob给植物j浇水
            if b < plants[j]:
                # 没有足够的水
                ans += 1
                b = capacityB
            b -= plants[j]
            j -= 1
        # Alice 和 Bob到达同一株植物，那么当前水罐中水更多的人会给这株植物浇水
        if i == j and max(a, b) < plants[i]:
            # 没有足够多的水
            ans += 1
        return ans


Solution().minimumRefill(
    plants=[726, 739, 934, 116, 643, 648, 473, 984, 482, 85, 850, 806, 146, 764, 156, 66, 186, 339, 985, 237, 662, 552,
            800, 78, 617, 933, 481, 652, 796, 594, 151, 82, 183, 241, 525, 221, 951, 732, 799, 483, 368, 354, 776, 175,
            974, 187, 913, 842], capacityA=1439, capacityB=1207)
