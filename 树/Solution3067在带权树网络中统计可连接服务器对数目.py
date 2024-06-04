from typing import List


class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = 1
        g = [[] for _ in range(1010)]
        for a, b, w in edges:
            n = max(a, b, n)
            g[a].append((b, w))
            g[b].append((a, w))

        n += 1

        def dfs(root: int, w: int, pre: int):
            cnt = 0
            if (w % signalSpeed) == 0:
                cnt += 1
            for node, weight in g[root]:
                if node == pre:
                    continue
                cnt += dfs(node, weight + w, root)
            return cnt

        count = []
        for i in range(n):
            path = []
            for j, w in g[i]:
                cnt = dfs(j, w, i)
                if cnt != 0:
                    path.append(cnt)
            tmp = 0
            if len(path) >= 2:
                for j in range(len(path)):
                    for k in range(j + 1, len(path)):
                        tmp += path[j] * path[k]
            count.append(tmp)
        return count

    def countPairsOfConnectableServers1(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for x, y, wt in edges:
            g[x].append((y, wt))
            g[y].append((x, wt))

        def dfs(x: int, fa: int, s: int):
            cnt = 0 if s % signalSpeed else 1
            for y, wt in g[x]:
                if y != fa:
                    cnt += dfs(y, x, s + wt)
            return cnt

        ans = [0] * n
        for i, gi in enumerate(g):
            s = 0
            for y, wt in gi:
                cnt = dfs(y, i, wt)
                ans[i] += cnt * s  # 两两互乘，变为一次遍历，小技巧
                s += cnt
        return ans


Solution().countPairsOfConnectableServers(edges=[[0, 1, 1], [1, 2, 5], [2, 3, 13], [3, 4, 9], [4, 5, 2]], signalSpeed=1)
