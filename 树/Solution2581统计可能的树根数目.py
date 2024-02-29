from typing import List


# 树形动态规划

# 首先计算固定树根时猜对的次数，假设以 0 号节点为树根，从它开始执行深度优先搜索，
# 使用哈希表统计所有树边 (x,y) 在 guesses 中出现的个数，
# 其中 x 是 y 的父节点。

# 然后考虑树根从 0 移动到 0 的子节点后，所有 guesses 的状态变化。如下图所示，树根从 x 变成 y 之后，
# 只有 (x,y) 和 (y,x)这两个猜测的正确性发生变化。

class Solution:
    # 超过时间限制
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        links = []
        visited = [False for _ in range(len(edges) + 1)]

        g = [[] for _ in range(len(edges) + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        queue = []

        def bfs(i):
            queue.append(i)
            while len(queue) != 0:
                j = queue.pop()
                visited[j] = True
                for node in g[j]:
                    if not visited[node]:
                        links.append([j, node])
                        queue.append(node)

        bfs(0)
        cnt = 0
        for link in links:
            if link in guesses:
                cnt += 1

        dict = {}
        dict[0] = cnt
        visited = [False for _ in range(len(edges) + 1)]

        def bfs_root(i):
            queue.append(i)
            ans = 0
            while len(queue) != 0:
                j = queue.pop()
                visited[j] = True
                cnt = dict[j]
                if cnt >= k:
                    ans += 1
                for node in g[j]:
                    if not visited[node]:
                        if [node, j] in guesses and [j, node] not in guesses:
                            dict[node] = cnt + 1
                        elif [node, j] not in guesses and [j, node] in guesses:
                            dict[node] = cnt - 1
                        else:
                            dict[node] = cnt
                        queue.append(node)
            return ans

        return bfs_root(0)

    # 改进，list查找时间太浪费，改为hash
    def rootCount1(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        links = []
        visited = [False for _ in range(len(edges) + 1)]

        g = [[] for _ in range(len(edges) + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        st = set()

        # 树边（x,y）哈希函数
        def h(x, y):
            return x << 20 | y  # 根据树有多少个节点计算

        for u, v in guesses:
            st.add(h(u, v))

        queue = []

        def bfs(i):
            queue.append(i)
            while len(queue) != 0:
                j = queue.pop()
                visited[j] = True
                for node in g[j]:
                    if not visited[node]:
                        links.append([j, node])
                        queue.append(node)

        bfs(0)
        cnt = 0
        for u, v in links:
            if h(u, v) in st:
                cnt += 1

        dict = {}
        dict[0] = cnt
        visited = [False for _ in range(len(edges) + 1)]

        def bfs_root(i):
            queue.append(i)
            ans = 0
            while len(queue) != 0:
                j = queue.pop()
                visited[j] = True
                cnt = dict[j]
                if cnt >= k:
                    ans += 1
                for node in g[j]:
                    if not visited[node]:
                        if h(node, j) in st and h(j, node) not in st:
                            dict[node] = cnt + 1
                        elif h(node, j) not in st and h(j, node) in st:
                            dict[node] = cnt - 1
                        else:
                            dict[node] = cnt
                        queue.append(node)
            return ans

        return bfs_root(0)

    def rootCount2(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        st = set()

        def h(x, y):
            return x << 20 | y

        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        for u, v in guesses:
            st.add(h(u, v))

        res, cnt = 0, 0

        def dfs(x, fat):
            nonlocal cnt
            for y in g[x]:
                if y == fat:
                    continue
                # 直接计算符合的猜想
                cnt += h(x, y) in st
                dfs(y, x)

        dfs(0, -1)

        def redfs(x, fat, cnt):
            nonlocal res
            if cnt >= k:
                res += 1
            for y in g[x]:
                if y == fat:
                    continue
                redfs(y, x, cnt - (h(x, y) in st) + (h(y, x) in st))

        redfs(0, -1, cnt)

        return res


Solution().rootCount2([[0, 1], [1, 2], [1, 3], [4, 2]], [[1, 3], [0, 1], [1, 0], [2, 4]], 3)
