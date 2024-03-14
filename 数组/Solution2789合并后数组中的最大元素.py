from typing import List


class Solution:
    # 倒序遍历数组
    def maxArrayValue(self, nums: List[int]) -> int:
        res = nums[-1]
        tmp = nums[-1]
        for i in range(len(nums) - 1, 0, -1):
            if tmp >= nums[i - 1]:
                tmp = tmp + nums[i - 1]
                res = max(tmp, res)
            else:
                tmp = nums[i - 1]
        return res if res >= nums[0] else nums[0]

    def maxArrayValue(self, nums: List[int]) -> int:
        # 合并完的数组肯定是递减的，因为后面的大数合并前面的小数，要是没被合并，肯定说明前面大，所以最大的肯定就是nums[0]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                nums[i] += nums[i + 1]
        return nums[0]


Solution().maxArrayValue(nums=[2, 3, 7, 9, 3])
Solution().maxArrayValue(nums=[91, 50])
