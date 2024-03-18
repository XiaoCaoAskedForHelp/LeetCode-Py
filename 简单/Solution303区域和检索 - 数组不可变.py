from itertools import accumulate
from typing import List


class NumArray:
    # 前缀和
    # def __init__(self, nums: List[int]):
    #     self.total = list(accumulate(nums, initial=0))
    #
    # def sumRange(self, left: int, right: int) -> int:
    #     return self.total[right + 1] - self.total[left]

    def __init__(self, nums: List[int]):
        self.sums = [0]
        for num in nums:
            self.sums.append(num + self.sums[-1])

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
