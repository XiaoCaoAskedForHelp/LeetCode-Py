# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from 动态规划.Solution337打家劫舍III import TreeNode


class FindElements:

    # def __init__(self, root: Optional[TreeNode]):
    #     self.st = set()
    #     if root:
    #         self.st.add(0)
    #         self.dfs(root, 0)
    #
    # def dfs(self, root: Optional[TreeNode], val):
    #     root.val = val
    #     if root.left:
    #         self.st.add(2 * val + 1)
    #         self.dfs(root.left, 2 * val + 1)
    #     if root.right:
    #         self.st.add(2 * val + 2)
    #         self.dfs(root.right, 2 * val + 2)
    #
    # def find(self, target: int) -> bool:
    #     return self.st.__contains__(target)

    # 深度优先搜索 + 哈希表

    def __init__(self, root: Optional[TreeNode]):
        self.valSet = set()
        self.dfs(root, 0)

    def dfs(self, node: TreeNode, val: int):
        if node is None:
            return
        node.val = val
        self.valSet.add(val)
        self.dfs(node.left, val * 2 + 1)
        self.dfs(node.right, val * 2 + 2)

    def find(self, target: int) -> bool:
        return target in self.valSet

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
