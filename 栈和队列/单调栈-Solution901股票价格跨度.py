from cmath import inf


class StockSpanner:
    # 寻找到左边小于等于当前值的最大连续天数（必须包括今天）
    # 其实就是寻找左边第一个大于当前值即可
    # 把小于等于当前值的都弹出栈
    # def __init__(self):
    #     # 存储的下标
    #     self.stack = []
    #     self.stock = []
    #
    # def next(self, price: int) -> int:
    #     if not self.stack or self.stock[self.stack[-1]] > price:
    #         self.stack.append(len(self.stock))
    #         self.stock.append(price)
    #         return 1
    #     else:
    #         while self.stack and self.stock[self.stack[-1]] <= price:
    #             self.stack.pop()
    #         res = len(self.stock) - (self.stack[-1] if self.stack else -1)
    #         self.stack.append(len(self.stock))
    #         self.stock.append(price)
    #         return res

    def __init__(self):
        self.stack = [(-1, inf)]  # 加入进来的股票下标和值,直接把值一起加入栈，这样就不用额外开一个数组存储值了
        self.idx = -1

    def next(self, price: int) -> int:
        self.idx += 1
        while price >= self.stack[-1][1]:
            self.stack.pop()
        self.stack.append((self.idx, price))
        return self.idx - self.stack[-2][0]


stockSpanner = StockSpanner()
# stockSpanner.next(100)
# stockSpanner.next(80)
# stockSpanner.next(60)
# stockSpanner.next(70)
# stockSpanner.next(60)
# stockSpanner.next(75)
# stockSpanner.next(85)

stockSpanner.next(31)
stockSpanner.next(41)
stockSpanner.next(48)
stockSpanner.next(59)
stockSpanner.next(79)

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
