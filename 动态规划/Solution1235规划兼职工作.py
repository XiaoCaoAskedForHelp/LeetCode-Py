import bisect
from collections import defaultdict
from typing import List


class Solution:
    # 超出内存限制，因为n可能会很大
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dic = defaultdict(list)
        for start, end, pro in zip(startTime, endTime, profit):
            dic[end].append((start, pro))
        n = max(endTime)  # 最晚到n天结束
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for start, pro in dic[i]:
                dp[i] = max(dp[start] + pro, dp[i])
        return max(dp)

    # 按照结束时间排序后的前 i 个工作的最大报酬
    def jobScheduling1(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted((zip(endTime, startTime, profit)))
        f = [0] * (len(jobs) + 1)
        for i, (end, start, p) in enumerate(jobs):
            # 上一个的结束时间在i的开始时间之前或者等于
            j = bisect.bisect_left(jobs, (start + 1,), hi=i)  # hi=i 表示二分上界为i（默认为n）
            f[i + 1] = max(f[i], f[j] + p)
        return f[-1]


Solution().jobScheduling(startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70])
