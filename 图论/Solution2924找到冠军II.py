from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[y].append(x)
        res = -1
        for idx, i in enumerate(g):
            if len(i) == 0:
                if res == -1:
                    res = idx
                else:
                    return -1
        return res

    # 标记所有 edges[i][1]，这些队伍都不是冠军。
    def findChampion1(self, n: int, edges: List[List[int]]) -> int:
        is_weak = [False] * n
        for _, y in edges:
            is_weak[y] = True  # 不是冠军
        ans = -1
        for i, weak in enumerate(is_weak):
            if weak:
                continue
            if ans != -1:
                return -1
            ans = i
        return ans
