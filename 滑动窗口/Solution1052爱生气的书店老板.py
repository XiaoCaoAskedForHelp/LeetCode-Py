from typing import List


class Solution:
    # 两部分之和，不生气的基础满意客户部分，和生气的能平复的客户部分
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        base = 0
        for i in range(n):
            if grumpy[i] == 0:
                base += customers[i]
        ran = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                ran += customers[i]
        j = minutes
        m = ran
        while j < n:
            ran = ran + (customers[j] if grumpy[j] else 0) - (customers[j - minutes] if grumpy[j - minutes] else 0)
            m = max(ran, m)
            j += 1
        return base + m

    # 上述的两部分可以一起算
    def maxSatisfied1(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        s = [0, 0]  # grumpy有两种状态，分别记录着两种状态的和
        max_s1 = 0
        for i, (c, g) in enumerate(zip(customers, grumpy)):
            s[g] += c
            if i < minutes - 1:  # 窗口长度不足minutes
                continue
            max_s1 = max(max_s1, s[1])
            if grumpy[i - minutes + 1]:
                s[1] -= customers[i - minutes + 1]  # 窗口最左边元素离开窗口，和上面的做法不同的是，上面是离开和加入是同时的，但是这边是先离开后一轮加入
        return s[0] + max_s1


Solution().maxSatisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], minutes=3)
