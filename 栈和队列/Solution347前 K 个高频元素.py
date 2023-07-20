from typing import List
import heapq
import numpy as np


class Solution:

    def compare_tuples(t1, t2):
        return t1[0] - t2[0]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 要统计元素出现频率
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1

        # 对频率排序，小顶堆
        pri_que = []
        # 用固定大小为k的小顶堆，扫描所有频率的数值
        # python中只有最小堆，没有最大堆（将所有元素取反，弹出的时候也取反）
        # 使用 heapq 模块来维护一个优先队列
        # 优先级从小到大
        for key, value in map.items():
            heapq.heappush(pri_que, (value, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)

        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        # 要统计元素出现频率
        map = {}
        for i in range(len(nums)):
            map[nums[i]] = map.get(nums[i], 0) + 1

        temp = heapq.nlargest(k, map.items(), key=lambda s: s[1])
        arr = np.array(temp)
        return arr[:, 0].tolist()
