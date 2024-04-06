from typing import List


class TreeAncestor:
    def __init__(self, edges: List[List[int]]):
        n = len(edges) + 1  # 节点个数
        m = n.bit_length()  # 最多跳log2n的步长
        g = [[] for _ in range(n)]
        for x, y in edges:  # 节点编号从0 开始
            g[x].append(y)
            g[y].append(x)

        depth = [0] * n
        pa = [[-1] * m for _ in range(n)]  # 保存每个节点上面2^i位置的祖先节点

        def dfs(x: int, fa: int) -> None:
            pa[x][0] = fa  # 2^0 走一步的祖先节点，就是父亲节点
            for y in g[x]:
                if y != fa:
                    depth[y] = depth[x] + 1
                    dfs(y, x)

        # 计算每个节点的深度
        dfs(0, -1)

        for i in range(m - 1):
            for x in range(n):
                p = pa[x][i]
                if p != -1:  # 如果p是能到的
                    pa[x][i + 1] = pa[p][i]
        self.depth = depth
        self.pa = pa

    # 得到走k步能到的祖先节点
    def get_Kth_ancestor(self, node: int, k: int):
        for i in range(k.bit_length()):
            if k >> i & 1:  # k的二进制从低到高第i位是1
                node = self.pa[node][i]
        return node

    # 返回x和y的最近公共祖先（节点编号从0开始）
    def get_lca(self, x: int, y: int):
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        # 使y和x在同一深度
        y = self.get_Kth_ancestor(y, self.depth[y] - self.depth[x])
        if y == x:
            return x
        # 步长从大到小，更快能找到结果
        for i in range(len(self.pa[x]) - 1, -1, -1):
            px, py = self.pa[x][i], self.pa[y][i]  # 走2^i步，看祖先节点是否一致
            if px != py:  # 跳了2^i步，发现组先节点不相等，则说明相同的祖先节点还需要走更远的步数
                x, y = px, py
            # 如果相等，则可能跳过，最近公共祖先可能在这个点之前，直接i-1，步数变小一点去探索，出发点不变
            # 最后x,y会停在与最近公共祖先只差一步的地方
        return self.pa[x][0]
