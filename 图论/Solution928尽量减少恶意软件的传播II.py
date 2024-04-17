import copy
from cmath import inf
from collections import Counter
from typing import List


class Solution:
    # 暴力将所有感染的节点，逐个枚举，然后去dfs，找到感染面积最小的情况
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)

        def dfs(x: int):
            nonlocal area
            nonlocal flag
            visited[x] = True
            area += 1
            if x in ini:
                flag = True
            for y, conn in enumerate(gra[x]):
                if conn and not visited[y] and y != x:
                    dfs(y)

        res = (inf, -1)
        initial.sort()
        for i in initial:
            ini = initial.copy()
            ini.remove(i)
            gra = copy.deepcopy(graph)
            visited = [False] * n
            for j in range(n):
                gra[i][j] = 0
                gra[j][i] = 0
            cnt = 0
            for j in range(n):
                if visited[j]:
                    continue
                area = 0
                flag = False
                dfs(j)
                if flag:
                    cnt += area
            if cnt < res[0]:
                res = (cnt, i)
        return res[1]

    # 逆向思维，从不在 initial 中的点 v 出发 DFS，在不经过 initial 中的节点的前提下，看看 v 是只能被一个点感染到，还是能被多个点感染到。
    # 如果 v 只能被点 x=initial[i] 感染到，那么在本次 DFS 过程中访问到的其它节点，也只能被点 x 感染到。
    def minMalwareSpread1(self, graph: List[List[int]], initial: List[int]) -> int:
        st = set(initial)
        vis = [False] * len(graph)

        def dfs(x: int):
            nonlocal node_id, size
            vis[x] = True
            size += 1
            for y, conn in enumerate(graph[x]):
                if conn == 0:
                    continue
                if y in st:
                    # 按照 924 题的状态机更新 node_id
                    # 注意避免重复统计，例如上图中的 0 有两条不同路径可以遇到 1
                    if node_id != -2 and node_id != y:  # 第一次碰到感染节点，就记录下来，说明只需要去掉一个节点就能解决感染
                        node_id = y if node_id == -1 else -2  # 如果第二次以上碰到就置为-2
                elif not vis[y]:
                    dfs(y)

        cnt = Counter()
        for i, seen in enumerate(vis):
            if seen or i in st:  # 枚举 [0,n−1] 中没有访问过的，且不在 initial 中的节点 i
                continue
            node_id = -1
            size = 0
            dfs(i)
            if node_id >= 0:  # 只找到一个在initial中的节点
                # 删除节点node_id可以让size个点不被感染
                cnt[node_id] += size
        # size取反计算最大值，相同最大值去node_id最小值
        return min((-size, node_id) for node_id, size in cnt.items())[1] if cnt else min(initial)


Solution().minMalwareSpread(graph=[[1, 1, 0, 0], [1, 1, 0, 1], [0, 0, 1, 0], [0, 1, 0, 1]], initial=[3, 0])
