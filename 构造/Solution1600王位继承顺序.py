from collections import defaultdict
from typing import List


class ThroneInheritance:

    # def __init__(self, kingName: str):
    #     self.dic = {kingName: []}  # 记录最后一个子孙的位置
    #     self.dic1 = {}  # 记录是否死亡
    #     self.root = kingName
    #
    # def birth(self, parentName: str, childName: str) -> None:
    #     self.dic[parentName].append(childName)
    #     self.dic[childName] = []
    #
    # def death(self, name: str) -> None:
    #     self.dic1[name] = True  # 记录死亡，但是不是真的删除
    #
    # def getInheritanceOrder(self) -> List[str]:
    #     def dfs(root: str):
    #         if not self.dic[root]:
    #             return
    #         for child in self.dic[root]:
    #             if not self.dic1.get(child):
    #                 res.append(child)
    #             dfs(child)
    #
    #     res = []
    #     if not self.dic1.get(self.root):
    #         res.append(self.root)
    #     dfs(self.root)
    #     return res

    # ThroneInheritance(kingName)：我们将kingName作为树的根节点；
    # birth(parentName,childName)：我们在树中添加一条从parentName到childName的边，将childName作为parentName的子节点；
    # death(name)：我们使用一个哈希集合记录所有的死亡人员，将name加入该哈希集合中；
    # getInheritanceOrder()：我们从根节点开始对整棵树进行前序遍历。需要注意的是，如果遍历到死亡人员，那么不能将其加入继承顺序列表中。
    def __init__(self, kingName: str):
        self.edges = defaultdict(list)
        self.dead = set()
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.edges[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = list()

        def preorder(name: str):
            if name not in self.dead:
                ans.append(name)
            if name in self.edges:
                for childName in self.edges[name]:
                    preorder(childName)

        preorder(self.king)
        return ans

# Your ThroneInheritance object will be instantiated and called as such:
obj = ThroneInheritance("king")
obj.birth("king","andy")
obj.death("andy")
param_3 = obj.getInheritanceOrder()
