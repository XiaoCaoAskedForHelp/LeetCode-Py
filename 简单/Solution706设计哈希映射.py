class MyHashMap:

    # def __init__(self):
    #     self.dict = [-1] * (10 ** 6 + 1)
    #
    # def put(self, key: int, value: int) -> None:
    #     self.dict[key] = value
    #
    # def get(self, key: int) -> int:
    #     return self.dict[key]
    #
    # def remove(self, key: int) -> None:
    #     self.dict[key] = -1

    # 我们存储的不是 key 本身，而是 (key,value) 对  链地址法
    def __init__(self):
        self.base = 769
        self.data = [[] for _ in range(self.base)]

    def hash(self, key):
        return key % self.base

    def put(self, key: int, value: int) -> None:
        h = self.hash(key)
        for item in self.data[h]:
            if item[0] == key:
                item[1] = value
                return
        self.data[h].append([key, value])

    def get(self, key: int) -> int:
        h = self.hash(key)
        for item in self.data[h]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        h = self.hash(key)
        for i, item in enumerate(self.data[h]):
            if item[0] == key:
                self.data[h].pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
