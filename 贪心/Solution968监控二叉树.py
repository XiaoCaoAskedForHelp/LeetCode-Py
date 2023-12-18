# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # Greedy Algo:
        # 从下往上安装摄像头：跳过leaves这样安装数量最少，局部最优 -> 全局最优
        # 先给leaves的父节点安装，然后每隔两层节点安装一个摄像头，直到Head
        # 0: 该节点未覆盖
        # 1: 该节点有摄像头
        # 2: 该节点有覆盖
        # 基本数据类型（如整数、浮点数、布尔值等）在函数调用时是按值传递的。这意味着当您将result传递给traversal函数时，传递的是result当前值的一个副本，而不是result本身。
        # result = 0
        # 要么变为result = [0] 使用列表进行传递，要么把 result 定义为类的一个属性
        self.result = 0
        if self.traversal(root) == 0:
            self.result += 1
        return self.result

    def traversal(self, cur: TreeNode):
        if not cur:
            return 2

        left = self.traversal(cur.left)
        right = self.traversal(cur.right)

        # 情况1: 左右节点都有覆盖
        if right == 2 and left == 2:
            return 0

        # 情况2:
        # left == 0 && right == 0 左右节点无覆盖
        # left == 1 && right == 0 左节点有摄像头，右节点无覆盖
        # left == 0 && right == 1 左节点无覆盖，右节点有摄像头
        # left == 0 && right == 2 左节点无覆盖，右节点覆盖
        # left == 2 && right == 0 左节点覆盖，右节点无覆盖
        if left == 0 or right == 0:
            self.result += 1
            return 1

        # 情况3:
        # left == 1 && right == 2 左节点有摄像头，右节点有覆盖
        # left == 2 && right == 1 左节点有覆盖，右节点有摄像头
        # left == 1 && right == 1 左右节点都有摄像头
        if left == 1 or right == 1:
            return 2
