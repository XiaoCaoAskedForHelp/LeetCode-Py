from typing import List


class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n = n  # 行数
        self.m = m  # 列数
        self.min = [0] * (n * 4)  # 区间被占用座位的最小值
        self.sum = [0] * (n * 4)  # 区间座位的总和

    # 返回区间 [1,R] 中 <= val 的最靠左的位置，不存在时返回 0
    def index(self, o: int, l: int, r: int, R: int, val: int):
        if self.min[o] > val:
            return 0  # 说明整个区间的元素值都大于val
        if l == r:
            return l
        m = (l + r) // 2
        if self.min[o * 2] <= val:
            return self.index(o * 2, l, m, R, val)  # 看看左半部分
        if m < R:
            return self.index(o * 2 + 1, m + 1, r, R, val)  # 看看右半部分
        return 0

    def query(self, o: int, l: int, r: int, L: int, R: int):
        if L <= l and r <= R: return self.sum[o]
        sum = 0
        m = (l + r) // 2
        if L <= m: sum += self.query(o * 2, l, m, L, R)
        if R > m: sum += self.query(o * 2 + 1, m + 1, r, L, R)
        return sum

    def add(self, o: int, l: int, r: int, idx: int, val: int):
        if l == r:
            self.min[o] += val
            self.sum[o] += val
            return
        m = (l + r) // 2
        if idx <= m:
            self.add(o * 2, l, m, idx, val)
        else:
            self.add(o * 2 + 1, m + 1, r, idx, val)
        self.sum[o] = self.sum[o * 2] + self.sum[o * 2 + 1]
        self.min[o] = min(self.min[o * 2], self.min[o * 2 + 1])

    def gather(self, k: int, maxRow: int) -> List[int]:
        i = self.index(1, 1, self.n, maxRow + 1, self.m - k)  # 如果没有任何一行有足够的空座位，那么就会返回0
        if i == 0: return []
        seats = self.query(1, 1, self.n, i, i)
        self.add(1, 1, self.n, i, k)  # 在第i行上增加k个位置
        return [i - 1, seats]

    def scatter(self, k: int, maxRow: int) -> bool:
        if (maxRow + 1) * self.m - self.query(1, 1, self.n, 1, maxRow + 1) < k:
            return False  # 前maxRow行剩余座位不足k个
        i = self.index(1, 1, self.n, maxRow + 1, self.m - 1)  # 从第一个没有坐满的排开始占座
        while True:
            left_seats = self.m - self.query(1, 1, self.n, i, i)
            if k <= left_seats:
                self.add(1, 1, self.n, i, k)
                return True
            k -= left_seats
            self.add(1, 1, self.n, i, left_seats)
            i += 1

        # Your BookMyShow object will be instantiated and called as such:


obj = BookMyShow(2, 5)
param_1 = obj.gather(4, 0)
param_1 = obj.gather(2, 0)
param_2 = obj.scatter(5, 1)
param_2 = obj.scatter(5, 1)
