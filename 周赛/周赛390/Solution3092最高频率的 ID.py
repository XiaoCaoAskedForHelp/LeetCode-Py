from collections import defaultdict
from typing import List

from sortedcontainers import SortedList


class Solution:
    # 超出时间限制
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        dic = defaultdict(int)
        ans = [0] * len(nums)
        for i in range(len(nums)):
            dic[nums[i]] += freq[i]
            ans[i] = max(dic.values())
        return ans

    # 优化寻找最大值
    def mostFrequentIDs1(self, nums: List[int], freq: List[int]) -> List[int]:
        dic = defaultdict(int)
        ans = [0] * len(nums)
        m = 0
        for i in range(len(nums)):
            if m == dic[nums[i]] and freq[i] < 0:
                dic[nums[i]] += freq[i]
                m = max(dic.values())
            else:
                dic[nums[i]] += freq[i]
                m = max(m, dic[nums[i]])
            ans[i] = m
        return ans

    def mostFrequentIDs2(self, nums: List[int], freq: List[int]) -> List[int]:
        sl = SortedList(key=lambda x: x[0])
        cnt = defaultdict(int)
        res = []
        for x, c in zip(nums, freq):
            if cnt[x] != 0:
                sl.remove((cnt[x], x))
            cnt[x] += c
            if cnt[x] != 0:
                sl.add((cnt[x], x))
            res.append(sl[-1][0] if sl else 0)
        return res
