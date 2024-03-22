from collections import defaultdict, Counter


class FrequencyTracker:

    # 超时
    # def __init__(self):
    #     self.dic = defaultdict(int)
    #
    # def add(self, number: int) -> None:
    #     self.dic[number] += 1
    #
    # def deleteOne(self, number: int) -> None:
    #     if self.dic[number]:
    #         self.dic[number] -= 1
    #
    # def hasFrequency(self, frequency: int) -> bool:
    #     for i in self.dic.values():
    #         if i == frequency:
    #             return True
    #     return False

    # def __init__(self):
    #     self.dic = defaultdict(int)
    #     self.fredic = defaultdict(int)
    #
    # def add(self, number: int) -> None:
    #     if self.fredic[self.dic[number]]:
    #         self.fredic[self.dic[number]] -= 1
    #     self.dic[number] += 1
    #     self.fredic[self.dic[number]] += 1
    #
    # def deleteOne(self, number: int) -> None:
    #     if self.dic[number]:
    #         if self.fredic[self.dic[number]]:
    #             self.fredic[self.dic[number]] -= 1
    #         self.dic[number] -= 1
    #         self.fredic[self.dic[number]] += 1
    #
    # def hasFrequency(self, frequency: int) -> bool:
    #     return self.fredic[frequency] > 0

    def __init__(self):
        self.freq = Counter()
        self.freq_cnt = Counter()

    def add(self, number: int) -> None:
        self.freq_cnt[self.freq[number]] -= 1  # 如果是0 的话减1对之后的操作也不会有影响
        self.freq[number] += 1
        self.freq_cnt[self.freq[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.freq[number] == 0:
            return
        self.freq_cnt[self.freq[number]] -= 1
        self.freq[number] -= 1
        self.freq_cnt[self.freq[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_cnt[frequency] > 0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
