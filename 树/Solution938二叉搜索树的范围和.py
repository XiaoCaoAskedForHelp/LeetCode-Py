from typing import Optional

from 动态规划.Solution337打家劫舍III import TreeNode


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node: TreeNode):
            nonlocal res
            if not node:
                return
            if node.val >= low and node.val <= high:
                res += node.val
            dfs(node.left)
            dfs(node.right)

        res = 0
        dfs(root)
        return res

    # 因为题目是二叉搜索树，所以不需要搜索整颗树
    def rangeSumBST1(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        elif root.val > high:
            return self.rangeSumBST1(root.left, low, high)
        elif root.val < low:
            return self.rangeSumBST1(root.right, low, high)
        else:
            return root.val + self.rangeSumBST1(root.right, low, high) + self.rangeSumBST1(root.left, low, high)
