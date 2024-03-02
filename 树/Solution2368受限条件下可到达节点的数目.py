from typing import List


class Solution:
    # 超出时间限制  变为set后就可以了
    # dfs
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        res = 1
        visited = [False for _ in range(n)]

        st = set(restricted)

        def dfs(i: int):
            nonlocal res
            visited[i] = True
            for node in g[i]:
                if not visited[node] and node not in st:
                    res += 1
                    dfs(node)

        dfs(0)
        return res

    # dfs
    def reachableNodes1(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        is_restrict = [False] * n
        for node in restricted:
            is_restrict[node] = True
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        cnt = 0

        def dfs(x, f):
            nonlocal cnt
            cnt += 1
            for y in g[x]:
                if y != f and not is_restrict[y]:
                    dfs(y, x)

        dfs(0, -1)
        return cnt

    # 并查集
    def reachableNodes2(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        is_restrict = [0] * n
        for x in restricted:
            is_restrict[x] = 1

        def find(x: int):
            if x != father[x]:
                father[x] = find(father[x])  # 节点 u 的父节点 变成根节点
            return father[x]

        def join(u, v):
            uf = find(u)
            vf = find(v)
            if u == v:
                return
            else:
                father[uf] = vf

        father = list(range(n))
        for u, v in edges:
            if is_restrict[u] or is_restrict[v]:
                continue
            join(u, v)

        cnt = 0
        root = find(0)
        for i in range(len(father)):
            if root == find(i):
                cnt += 1
        return cnt

    # 并查集
    def reachableNodes3(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        is_restrict = [0] * n
        for x in restricted:
            is_restrict[x] = 1

        def find(x: int):
            if x != father[x]:
                father[x] = find(father[x])
            return father[x]

        def join(u, v):
            uf = find(u)
            vf = find(v)
            if uf != vf:
                # 让rank小的挂载在rank大的树上
                if rank[uf] > rank[vf]:
                    father[vf] = uf
                elif rank[uf] < rank[vf]:
                    father[uf] = vf
                else:
                    father[uf] = vf
                    rank[vf] += 1

        father = list(range(n))
        rank = [0] * n
        for u, v in edges:
            if is_restrict[u] or is_restrict[v]:
                continue
            join(u, v)

        cnt = 0
        root = find(0)
        for i in range(len(father)):
            if root == find(i):
                cnt += 1
        return cnt
