import heapq
from cmath import inf
from typing import List


class Solution:
    # 将工资组中单位质量所需花费最大的（ri）作为基础去计算工资，这就是发最低期望工资的那个工人
    # 其他单位工作质量工资（r）比他小的工人，发给他们的工资都是比期望工资大的，这些工人是可以随便选择的
    # k名工人的quality之和是sumQ，以ri为基准发工资，发的工资总额是sumQ1*ri，所以只要sumQ越少，在ri为基础的情况下，最后就是最少的
    # 通过最大堆维护一个当前最小的k个quality值
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs = sorted(zip(quality, wage), key=lambda p: p[1] / p[0])  # 通过单位质量花费r值进行排序
        h = [-q for q, _ in pairs[:k]]  # 先拿出前k个作为一组，后面在通过枚举进行比较，最大堆
        heapq.heapify(h)
        sum_q = -sum(h)
        ans = sum_q * pairs[k - 1][1] / pairs[k - 1][0]  # 后面的是r值大的，所以拿后面的作为基底
        for q, w in pairs[k:]:  # 枚举后面的工人作为基底，因为后面的工人r值更大
            if q < -h[0]:  # 虽然r值变大的了，但是sum_q会变的更小，可能会得到更小的答案
                sum_q += heapq.heapreplace(h, -q) + q  # 返回之前最大的那个的负数，并将现在这个放进去
                ans = min(ans, sum_q * w / q)
        return ans
