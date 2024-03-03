from typing import List


class Solution:
    #
    # dfs走一遍，跟dfs方向一样的就是需要改的
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res = 0
        g = [[] for _ in range(n)]
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)

        st = set()

        def h(x, y):
            return x << 20 | y

        for u, v in connections:
            st.add(h(u, v))

        def dfs(x: int, pre: int):
            nonlocal res
            for y in g[x]:
                if y != pre:
                    dfs(y, x)
                    if h(x, y) in st:
                        res += 1

        dfs(0, -1)
        return res

    # 超出时间限制
    def minReorder1(self, n: int, connections: List[List[int]]) -> int:
        count = 0
        st = {0}
        while True:
            for x, y in connections:
                if y in st:
                    st.add(x)  # 可以指向0
                elif x in st:
                    st.add(y)  # 反方向不能指向0
                    count += 1
            if len(st) == n:
                return count

    def minReorder2(self, n: int, connections: List[List[int]]) -> int:
        e = [[] for _ in range(n)]
        for edge in connections:
            e[edge[0]].append([edge[1], 1])
            e[edge[1]].append([edge[0], 0])
        return self.dfs(0, -1, e)

    def dfs(self, x: int, pre: int, e: List[List[List[int]]]):
        res = 0
        for edge in e[x]:
            if edge[0] == pre:
                continue
            res += edge[1] + self.dfs(edge[0], x, e)
        return res


Solution().minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]])
