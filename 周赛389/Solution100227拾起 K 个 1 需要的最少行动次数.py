from cmath import inf
from itertools import accumulate
from typing import List


class Solution:
    # 1.先收集index，index+1，index-1位置上的1
    # 2. 使用第一种操作+ 第二种操作，操作两次得到一个1
    # 3. index附近的1距离之和
    #
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        pos = []
        c = 0  # nums中连续的1 的长度
        for i, x in enumerate(nums):
            if x == 0:
                continue
            pos.append(i)  # 记录1的位置
            c = max(c, 1)
            if i > 0 and nums[i - 1] == 1:
                if i > 1 and nums[i - 2] == 1:
                    c = 3  # 有3个连续的1
                else:
                    c = max(c, 2)  # 有两个连续的1

        c = min(c, k)
        if maxChanges >= k - c:
            # 其余k-c个1全部可以用两次操作得到
            return max(c - 1, 0) + (k - c) * 2

        n = len(pos)
        pre_sum = list(accumulate(pos, initial=0))

        ans = inf
        # 除了max_changes个数可以用两次操作得到，其余的1只能一步步移动到pos[i]
        size = k - maxChanges
        for right in range(size, n + 1):
            # s1+s2 是j在[left，right）中的所有 pos[j] 到 pos[(left+right)/2] 的距离之和
            left = right - size
            i = left + size // 2
            s1 = pos[i] * (i - left) - (pre_sum[i] - pre_sum[left])  # i之前的几个数需要操作的次数
            s2 = pre_sum[right] - pre_sum[i] - pos[i] * (right - i)  # i之后的几个数需要操作的次数
            ans = min(ans, s1 + s2)
        return ans + maxChanges * 2
