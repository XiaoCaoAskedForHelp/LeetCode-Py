from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        p = [i for i in range(n)]
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]
        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu != pv:
                p[pu] = pv
        return find(source) == find(destination)