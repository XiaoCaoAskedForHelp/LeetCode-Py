from typing import List


class Solution:
    # 贪心其实就是找比较的小的数字，如果把小的数字排前面，如果小的数字比较后，不能满足k个数的条件，那可以将大一点的数加进去
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        for i, num in enumerate(nums):
            if not res:
                res.append(num)
            else:
                if res[-1] > num:
                    while res and res[-1] > num and n - i + len(res) > k:
                        res.pop()
                    res.append(num)
                else:
                    if len(res) < k:  # 如果长度不够就大的数字就可以直接加入进去
                        res.append(num)
        return res

    # 返回nums的长度恰好为k的字典序的最小子序列
    def mostCompetitive1(self, nums: List[int], k: int) -> List[int]:
        st = []
        for i, x in enumerate(nums):
            while st and x < st[-1] and len(st) + len(nums) - i > k:
                st.pop()
            if len(st) < k:
                st.append(x)
        return st
