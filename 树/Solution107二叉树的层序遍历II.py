# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import List, Optional

from sortedcontainers import SortedDict

from 动态规划.Solution337打家劫舍III import TreeNode


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict = [[] for _ in range(2001)]

        def digui(root: TreeNode, index):
            if not root:
                return
            digui(root.left, index + 1)
            dict[index].append(root.val)
            digui(root.right, index + 1)

        digui(root, 0)

        res = []
        for i in range(2000, -1, -1):
            if dict[i]:
                res.append(dict[i])
        return res

    # 广度优先搜索层序遍历，从上到下
    def levelOrderBottom1(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelOrder = []
        if not root:
            return levelOrder

        q = deque([root])
        while q:
            level = []
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levelOrder.append(level)
        return levelOrder[::-1]


Solution().levelOrderBottom1(TreeNode(1))
