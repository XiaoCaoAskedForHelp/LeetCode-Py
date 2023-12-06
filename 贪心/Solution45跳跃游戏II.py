from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        cur_distance = 0
        ans = 0
        next_distance = 0

        for i in range(len(nums)):
            next_distance = max(nums[i] + i, next_distance)
            if i == cur_distance:
                ans += 1
                cur_distance = next_distance
                if cur_distance >= len(nums) - 1:
                    break
        return ans

    def jump1(self, nums: List[int]) -> int:
        cur_distance = 0  # 当前覆盖的最远距离下标
        ans = 0  # 记录走的最大步数
        next_distance = 0  # 下一步覆盖的最远距离下标

        for i in range(len(nums) - 1):  # 注意这里是小于len(nums) - 1，这是关键所在
            next_distance = max(nums[i] + i, next_distance)  # 更新下一步覆盖的最远距离下标
            if i == cur_distance:  # 遇到当前覆盖的最远距离下标
                cur_distance = next_distance  # 更新当前覆盖的最远距离下标
                ans += 1

        return ans

    # 贪心（版本三） 类似‘55 - 跳跃游戏’写法
    def jump2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        i = 0
        count = 0
        cover = 0
        while i <= cover:
            for i in range(i, cover + 1):
                cover = max(nums[i] + i, cover)
                if cover >= len(nums) - 1:
                    return count + 1
            count += 1

    def jump3(self, nums: List[int]) -> int:
        result = [10 ** 4 + 1] * len(nums)  # 初始化结果数组，初始值为一个较大的数
        result[0] = 0

        for i in range(len(nums)):
            for j in range(nums[i] + 1):
                if i + j < len(nums):
                    result[i + j] = min(result[i + j], result[i] + 1);
        return result[-1]
