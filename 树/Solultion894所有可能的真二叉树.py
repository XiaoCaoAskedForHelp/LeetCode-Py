# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from 动态规划.Solution337打家劫舍III import TreeNode


class Solution:
    # 当n是奇数时，n个结点的真二叉树满足左子树和右子树的结点数都是奇数，此时左子树和右子树的结点数之和是n−1，假设左子树的数目为i，则左子树的节点数目则为n−1− i
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        res = []
        if n % 2 == 0:
            return []
        if n == 1:
            res.append(TreeNode(0))
        # 枚举左子树可能的节点的个数
        for i in range(1, n, 2):
            lefts = self.allPossibleFBT(i)
            rights = self.allPossibleFBT(n - 1 - i)
            for left in lefts:
                for right in rights:
                    root = TreeNode(0, left, right)  # 左子树和右子树拼起来就是子真二叉树
                    res.append(root)
        return res  # 返回上一层继续拼接

    # dp
    def allPossibleFBT1(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        dp = [[] for _ in range(n + 1)]
        dp[1] = [TreeNode(0)]
        for i in range(3, n + 1, 2):  # 列出可能出现的节点个数3,5,7，。。。
            for j in range(1, i, 2):  # 列出左子树的节点个数
                for left in dp[j]:
                    for right in dp[i - 1 - j]:
                        root = TreeNode(0, left, right)
                        dp[i].append(root)
        return dp[n]

    # 由于每增加 2 个节点，真二叉树就会多 1 个叶子，所以一棵有 n 个节点的真二叉树恰好有 n+1/2个叶子。
    # 枚举叶子，n=7有4个叶子，左1右3，左2右2，左3右1
    def allPossibleFBT2(self, n: int) -> List[Optional[TreeNode]]:
        MX = 11  # 根据题目最多就是11个叶子节点
        f = [[] for _ in range(MX)]
        f[1] = [TreeNode(0)]
        for i in range(2, MX):
            f[i] = [TreeNode(0, left, right)
                    for j in range(1, i)  # 枚举左子树叶子数
                    for left in f[j]  # 枚举左子树
                    for right in f[i - j]]  # 枚举右子树
        return f[(n + 1) // 2] if n % 2 else []


Solution().allPossibleFBT1(7)
