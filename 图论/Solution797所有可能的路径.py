from typing import List


class Solution:
    def __init__(self):
        self.res = []
        self.path = [0]
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []
        self.dfs(graph, 0)
        return self.res

    def dfs(self, graph, index):
        if index == len(graph) - 1:# 成功找到一条路径时
            # path是引用，需要复制一份
            self.res.append(self.path[:])
            return
        for i in graph[index]:  # 遍历节点n的所有邻接节点
            self.path.append(i)
            self.dfs(graph, i)
            self.path.pop()  # 回溯

