# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

from 动态规划.Solution337打家劫舍III import TreeNode


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = deque([cloned])
        while queue:
            node = queue.popleft()
            if node.val == target.val:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return None

    # 同时对二叉树 original与 cloned 进行深度优先搜索
    def getTargetCopy1(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        if original == target:
            return cloned
        left = self.getTargetCopy1(original.left, cloned.left, target)
        if left:  # 如果左边搜索到了，就不用搜索右边了
            return left
        return self.getTargetCopy1(original.right, cloned.right, target)

    # 使用队列同时对二叉树 original 和 cloned 进行广度优先搜索
    def getTargetCopy2(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q1, q2 = [original], [cloned]
        while q1:
            node1, node2 = q1[0], q2[0]
            q1, q2 = q1[1:], q2[1:]
            if node1 == target:
                return node2
            if node1.left is not None:
                q1.append(node1.left)
                q2.append(node2.left)
            if node1.right is not None:
                q1.append(node1.right)
                q2.append(node2.right)
        return None
