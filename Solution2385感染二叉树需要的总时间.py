# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from functools import cache
from typing import Optional

from 动态规划.Solution337打家劫舍III import TreeNode


class Solution:
    # 记录父节点 + 两次DFS
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        fa = {}
        start_Node = None

        def dfs(node: TreeNode, pre: TreeNode):
            if node is None:
                return
            fa[node] = pre  # 记录每个节点的父节点
            if node.val == start:  # 找到start
                nonlocal start_Node
                start_Node = node
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        def maxDepth(node: TreeNode, pre: TreeNode):
            if node is None:
                return -1
            return max(maxDepth(x, node) for x in (node.left, node.right, fa[node]) if x != pre) + 1

        return maxDepth(start_Node, start_Node)

    # 我们先通过一次 DFS 建图，得到一个邻接表 ggg，其中 g[node] 表示与节点 node 相连的所有节点。
    # 然后，我们以 start 作为起点，通过 DFS 搜索整棵树，找到最远距离，即为答案。
    def amountOfTime1(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node: TreeNode, fa: TreeNode):
            if node is None:
                return
            if fa:
                g[node.val].append(fa.val)
                g[fa.val].append(node.val)
            dfs(node.left, node)
            dfs(node.right, node)

        def dfs2(node: int, fa: int) -> int:
            ans = 0
            for nxt in g[node]:
                if nxt != fa:
                    ans = max(ans, 1 + dfs2(nxt, node))
            return ans

        g = defaultdict(list)
        dfs(root, None)
        return dfs2(start, -1)

    # 一次dfs，树的直径
    def amountOfTime2(self, root: Optional[TreeNode], start: int) -> int:
        ans = 0

        def dfs(node: TreeNode):
            if node is None:
                return 0, False
            l_len, l_found = dfs(node.left)
            r_len, r_found = dfs(node.right)
            # 上述已经得到了这个节点的左右深度
            nonlocal ans
            if node.val == start:
                # 计算字数start的最大深度
                ans = max(l_len, r_len)
                return 1, True  # 找到了start
            if l_found or r_found:
                # 只有在左子树和右子树包含start时，才能更新答案，以每一个节点作为转折点计算他的左右最大长度，树的直径就是其中的最大值
                ans = max(ans, l_len + r_len)  # 两条链拼成直径
                return (l_len if l_found else r_len) + 1, True
            return max(l_len, r_len) + 1, False

        dfs(root)
        return ans

