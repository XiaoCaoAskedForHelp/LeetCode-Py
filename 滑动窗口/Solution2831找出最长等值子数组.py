from collections import defaultdict
from typing import List


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos_lists = defaultdict(list)
        # 记录每个相同数字的下标
        for i, x in enumerate(nums):
            pos_lists[x].append(i)
        left = 0
        # right - left + 1是等值子数组的长度
        # pos[right] - pos[left] + 1是原数组中的长度
        # 所以需要删除的就是 (pos[right] - pos[left] + 1) - (right - left + 1) = pos[right] - pos[left] - right + left
        res = 0
        for key in pos_lists.keys():
            left = 0
            for right, x in enumerate(pos_lists[key]):
                while pos_lists[key][right] - pos_lists[key][left] - right + left > k:
                    left += 1
                    if left > len(nums):
                        break
                if left > len(nums):
                    break
                res = max(res, right - left + 1)
        return res

    # pos可以直接保存pos[i] - i
    def longestEqualSubarray1(self, nums: List[int], k: int) -> int:
        pos_lists = defaultdict(list)
        for i, x in enumerate(nums):
            pos_lists[x].append(i - len(pos_lists[x]))
        ans = 0
        for pos in pos_lists.values():
            if len(pos) <= ans:
                continue  # 无法让ans变的更大
            left = 0
            # 直接遍历滑动窗口的右端
            for right, p in enumerate(pos):
                while p - pos[left] > k:  # 要删除的东西太多了
                    left += 1
                ans = max(ans, right - left + 1)
        return ans

    # ---------------------------------------------------------------------

    # 把删除多个数改为修改最多k个数
    # 思路和删除k个数是没有差别的，都是要分组找ops
    # 但是最终长度有区别
    def longestEqualSubarray2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pos_list = defaultdict(list)
        for i, x in enumerate(nums):
            pos_list[x].append(i)

        ans = 0
        for pos in pos_list.values():
            max_len = len(pos) + k
            if max_len >= n:  # 列表里面的所有数都可以修改成当前数，直接返回列表长度
                return n
            if max_len <= ans:  # 全修改了也无法让ans变的更大
                continue
            left = 0
            for right, p in enumerate(pos):
                while p - pos[left] - (right - left) > k:  # 要修改的数太多了
                    left += 1
                # 1.因为是修改而不是删除，所以修改的部分也作为总长的一部分
                # 2.下标差pos[right] - pos[left] + 1就是我们要的答案
                # 3. 最后还要和right - left + 1 + k 比较大小
                # 因为修改完两个下标中间区域的数，剩余修补次数还可以用来在开头或者末尾延长长度
                ans = max(ans, pos[right] - pos[left] + 1, right - left + 1 + k)
        return ans

    def longestEqualSubarray2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pos_lists = defaultdict(list)
        for i, x in enumerate(nums):
            pos_lists[x].append(i - len(pos_lists[x]))
        ans = 0
        for pos in pos_lists.values():
            max_len = len(pos) + k
            if max_len >= n:  # 列表里所有其他数都可以修改成当前数，直接返回列表长度
                return n
            if max_len <= ans:  # 全修改了也无法让 ans 变得更大
                continue
            left = 0
            for right, p in enumerate(pos):
                while p - pos[left] > k:  # 要修改的次数太多
                    left += 1
                # 下标index[i] = pos[i] + i，因为pos[i]记录的是index[i] - i
                ans = max(ans, right - left + 1 + k, pos[right] + right - (pos[left] + left) + 1)
        return ans
