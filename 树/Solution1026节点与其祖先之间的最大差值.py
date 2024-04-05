# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from 动态规划.Solution337打家劫舍III import TreeNode


class Solution:
    # dfs 求出每个节点的作为跟时，树上其他节点的最大值和最小值，就可以求出最终的差值
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            nonlocal res
            if not root.right and not root.left:
                return root.val, root.val
            rmax = lmax = 0
            rmin = lmin = 10 ** 5 + 5
            if root.right:
                rmax, rmin = dfs(root.right)
            if root.left:
                lmax, lmin = dfs(root.left)
            max1 = max(lmax, rmax)
            min1 = min(rmin, lmin)
            res = max(res, abs(root.val - max1), abs(root.val - min1))
            return max(max1, root.val), min(min1, root.val)

        res = 0
        dfs(root)
        return res

    # 枚举子孙节点，然后找出它的所有祖先节点，计算绝对差值
    # 并非所有祖先节点都需要被考虑到，我们只需要获取最小的祖先节点以及最大的祖先节点
    def maxAncestorDiff1(self, root: Optional[TreeNode]) -> int:
        def dfs(root, mi, ma):
            if not root:
                return 0
            diff = max(abs(root.val - mi), abs(root.val - ma))
            mi = min(root.val, mi)
            ma = max(root.val, ma)
            diff = max(diff, dfs(root.left, mi, ma))  # 遍历左子树，将它的父亲的节点的最大最小值传下去
            diff = max(diff, dfs(root.right, mi, ma))
            return diff  # 比较了左子树和右子树的最大差值就是结果（根左右）

        return dfs(root, root.val, root.val)

    # 递归到空节点时，mx 是从根到叶子的路径上的最大值，mn 是从根到叶子的路径上的最小值，所以 mx−mn 就是从根到叶子的路径上任意两点的最大差值。
    def maxAncestorDiff2(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: TreeNode, mn: int, mx: int):
            if node is None:
                nonlocal ans
                ans = max(ans, mx - mn)
                return
            mn = min(mn, node.val)
            mx = max(mx, node.val)
            dfs(node.left, mn, mx)
            dfs(node.right, mn, mx)

        dfs(root, root.val, root.val)
        return ans
