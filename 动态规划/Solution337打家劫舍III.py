# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    memory = {}

    def rob(self, root: Optional[TreeNode]) -> int:
        # 记忆化递归
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        if self.memory.get(root):
            return self.memory[root]
        # 偷父亲节点
        val1 = root.val
        if root.left:
            val1 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val1 += self.rob(root.right.left) + self.rob(root.right.right)

        # 不偷父亲节点
        val2 = self.rob(root.left) + self.rob(root.right)
        self.memory[root] = max(val1, val2)
        return max(val1, val2)

    def rob1(self, root: Optional[TreeNode]) -> int:
        # dp数组（dp table）以及下标的含义：
        # 1. 下标为 0 记录 **不偷该节点** 所得到的的最大金钱
        # 2. 下标为 1 记录 **偷该节点** 所得到的的最大金钱
        dp = self.robTree(root)
        return max(dp)

    def robTree(self, root: Optional[TreeNode]):
        if not root:
            return (0, 0)
        left = self.robTree(root.left)
        right = self.robTree(root.right)

        # 不偷cur，可以偷子节点
        val0 = max(left) + max(right)
        # 偷cur，不偷子节点
        val1 = root.val + left[0] + right[0]

        return (val0, val1)
