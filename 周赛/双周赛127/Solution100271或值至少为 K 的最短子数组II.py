from typing import List


class Solution:
    # 从0 开始找到一个子序列大于k，然后加入一个数，尝试在前端删除一些数来让序列长度最小
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def add(x):
            nonlocal cur
            for j in range(32):
                if x & 1 << j:
                    cnt[j] += 1
                    if cnt[j] == 1:  # 这个二进制位上之前没有过，这样或运算会加上这一位的值
                        cur += (1 << j)

        def remove(x):
            nonlocal cur
            for j in range(32):
                if x & (1 << j):
                    cnt[j] -= 1
                    if cnt[j] == 0:
                        cur -= (1 << j)

        n = len(nums)
        st = 0  # 序列开始下标
        cnt = [0] * 32  # 序列中每个二进制位的个数
        cur = 0  # 现在这个子序列的大小
        ans = n + 1  # 序列的长度
        for ed in range(n):
            add(nums[ed])
            while st <= ed and cur >= k:  # 当前序列大于等于k，就可以尝试从序列前端删除一些数字来让序列长度减少
                ans = min(ans, ed - st + 1)  # 先计算满足条件的长度，然后在尝试删除
                # 为什么可以删除但是不用回退呢，因为回退没有必要，原序列已经记载过最短长度，回退到原序列在加上后面的数组，只会更长，并不不会改变最小长度，还不如直接删到不符合k，在往后加数字
                remove(nums[st])
                st += 1
        if ans > n:
            return -1
        return ans
