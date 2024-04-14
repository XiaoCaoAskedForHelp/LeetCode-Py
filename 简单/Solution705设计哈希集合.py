class MyHashSet:

    # def __init__(self):
    #     self.container = []
    #
    # def add(self, key: int) -> None:
    #     if key not in self.container:
    #         self.container.append(key)
    #
    # def remove(self, key: int) -> None:
    #     if key in self.container:
    #         self.container.remove(key)
    #
    #
    # def contains(self, key: int) -> bool:
    #     if key in self.container:
    #         return True
    #     else:
    #         return False

    # 使用超大数组来解决本题是因为输入数据的范围在 0<=key<=10^6。因此我们只需要 10^6+1大小的数组，就能让每个数据都有一个单独的索引，不会有 key 的碰撞问题。
    # def __init__(self):
    #     self.set = [False] * (10 ** 6 + 1)
    #
    # def add(self, key: int) -> None:
    #     self.set[key] = True
    #
    # def remove(self, key: int) -> None:
    #     self.set[key] = False
    #
    # def contains(self, key: int) -> bool:
    #     return self.set[key]

    # 链地址法
    def __init__(self):
        self.buckets = 1000
        self.table = [[] for i in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def add(self, key: int) -> None:
        hashkey = self.hash(key)
        if key in self.table[hashkey]:
            return
        self.table[hashkey].append(key)

    def remove(self, key: int) -> None:
        hashkey = self.hash(key)
        if key not in self.table[hashkey]:
            return
        self.table[hashkey].remove(key)

    def contains(self, key: int) -> bool:
        hashkey = self.hash(key)
        return key in self.table[hashkey]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
