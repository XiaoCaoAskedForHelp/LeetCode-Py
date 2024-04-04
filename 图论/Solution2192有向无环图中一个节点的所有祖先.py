from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def dfs(x):
            if visited[x]:
                return dp[x]
            # 如果到了最上面的父亲节点
            nodes = g[x]
            if not nodes:
                visited[x] = True
                return []
            tmp = set()
            tmp.update(nodes)
            for i in nodes:
                tmp.update(dfs(i))
            visited[x] = True
            dp[x] = sorted(list(tmp))
            return dp[x]

        g = [[] for i in range(n)]
        f = [[] for i in range(n)]
        for u, v in edges:
            g[v].append(u)  # 记录它的祖先节点
            f[u].append(v)
        lasts = []
        for i in range(n):
            if not f[i]:
                lasts.append(i)

        dp = [[] for i in range(n)]
        visited = [False for i in range(n)]
        for i in lasts:
            dfs(i)

        return dp

    # 把边反向，从点 i 出发 DFS，能访问到的点就是 answer[i]。
    def getAncestors1(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[y].append(x)  # 反向建图

        def dfs(x: int):
            vis[x] = True  # 避免重复访问
            for y in g[x]:
                if not vis[y]:
                    dfs(y)  # 只递归没有访问过的点

        ans = [None] * n
        for i in range(n):
            vis = [False] * n
            dfs(i)  # 从i开始DFS
            vis[i] = False  # ans[i] 不含 i
            ans[i] = [j for j, b in enumerate(vis) if b]
        return ans

    # 正向dfs，比如从 2 出发 DFS，可以访问到 4,6,7，那么把 2 加到 answer[4],answer[6],answer[7] 中。
    def getAncestors2(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)

        def dfs(x):
            vis[x] = start
            for y in g[x]:
                if vis[y] != start:
                    ans[y].append(start)
                    dfs(y)

        ans = [[] for _ in range(n)]
        vis = [-1] * n
        for start in range(n):
            dfs(start)
        return ans


print(Solution().getAncestors(n=5,
                              edges=[[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]))
