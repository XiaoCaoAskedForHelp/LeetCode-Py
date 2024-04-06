from collections import deque
from typing import List


class TreeAncestor:
    # 超时
    # def __init__(self, n: int, parent: List[int]):
    #     self.parent = parent
    #
    # def getKthAncestor(self, node: int, k: int) -> int:
    #     for i in range(k):
    #         node = self.parent[node]
    #         if node == -1:
    #             return -1
    #     return node

    # 超出内存限制
    # def __init__(self, n: int, parent: List[int]):
    #     # 直接把每个节点的父亲节点都存好，查找的时候就是o(1)的复杂度
    #     g = [[] for _ in range(n)]
    #     for i in range(1, n):
    #         g[parent[i]].append(i)
    #     queue = deque([0])
    #     dp = [dict() for _ in range(n)]
    #     while queue:
    #         p = queue.popleft()
    #         dic = dp[p]
    #         for x in g[p]:
    #             dp[x].update(dic)
    #             idx = max(dp[x].keys()) if dp[x] else 0
    #             dp[x][idx + 1] = p
    #             queue.append(x)
    #     self.dp = dp
    #
    # def getKthAncestor(self, node: int, k: int) -> int:
    #     if not self.dp[node]:
    #         return -1
    #     m = max(self.dp[node].keys())
    #     return self.dp[node][m - k + 1] if self.dp[node].get(m - k + 1) is not None else -1

    # 预处理出每个节点的「爷爷节点」，即父节点的父节点，那么就可以两步两步地往上跳，从而减少一半的跳跃次数（循环次数）。
    # 预处理出每个节点的第2^i个祖先节点，记作 pa[x][i]
    # pa[x][i+1]=pa[pa[x][i]][i]，表示 x 的第 2^i个祖先节点的第 2^i个祖先节点就是 x 的第 2^i+1 个祖先节点
    def __init__(self, n: int, parent: List[int]):
        m = n.bit_length() - 1
        pa = [[p] + [-1] * m for p in parent]
        for i in range(m):
            for x in range(n):
                p = pa[x][i]
                if p != -1:
                    pa[x][i + 1] = pa[p][i]
        self.pa = pa

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(k.bit_length()):
            if (k >> i) & 1:  # k的二进制从低到高
                node = self.pa[node][i]
                if node < 0:
                    break
        return node

    def getKthAncestor1(self, node: int, k: int) -> int:
        while k and node != -1:
            lb = k & -k  # 获取一个二进制数的最低位的非零位
            node = self.pa[node][lb.bit_length() - 1]
            k ^= lb
        return node


# Your TreeAncestor object will be instantiated and called as such:
obj = TreeAncestor(n=7, parent=[-1, 0, 0, 1, 1, 2, 2])
print(obj.getKthAncestor1(3, 1))
