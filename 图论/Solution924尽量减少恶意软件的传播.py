import heapq
from typing import List


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        if n == 1:
            return initial[0]

        def dfs(x: int):
            nonlocal nodes
            nonlocal area
            for y in range(n):
                if x == y or graph[x][y] == 0 or visited[y]:
                    continue
                area += 1
                if y in ini:
                    nodes.append(y)
                visited[y] = True
                dfs(y)

        # 某一块连通子图中只有一个点是被感染的，那移除有效果，不然无效果。移除最小的就行
        initial.sort()
        ini = initial.copy()
        visited = [False] * n
        res = []
        while initial:
            nodes = []
            area = 1
            visited[initial[0]] = True
            tmp = initial[0]
            dfs(tmp)
            initial.remove(tmp)
            if not nodes:
                heapq.heappush(res, (-area, tmp))
            else:
                for i in nodes:
                    initial.remove(i)
        return heapq.heappop(res)[0] if res else ini[0]

    # 要找的是只包含一个被感染节点的连通块，并且这个连通块越大越好
    def minMalwareSpread1(self, graph: List[List[int]], initial: List[int]) -> int:
        st = set(initial)
        vis = [False] * len(graph)

        def dfs(x: int):
            vis[x] = True
            nonlocal node_id, size
            size += 1
            # 按照状态机更新node_id,只能找到一次x，第二次就会变为-2且不会变化了
            if node_id != -2 and x in st:
                node_id = x if node_id == -1 else -2
            for y, conn in enumerate(graph[x]):
                if conn and not vis[y]:
                    dfs(y)

        ans = -1
        max_size = 0
        for x in initial:
            if vis[x]:
                continue
            node_id = -1
            size = 0
            dfs(x)
            if node_id >= 0 and (size > max_size or size == max_size and node_id < ans):
                ans = node_id
                max_size = size
        return min(initial) if ans < 0 else ans


Solution().minMalwareSpread(graph=[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]], initial=[3, 1])
