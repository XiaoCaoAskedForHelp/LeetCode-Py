from functools import cache
from typing import List

import cachetools


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        nums = []

        # 不能加cache，cache只能保存返回值,添加操作是不会做的，只能正常dfs
        def dfs(k: int, n: int):
            if k < 0 or n < 0 or (k == 0 and n > 0) or (k > 0 and n == 0):
                return
            if k == 0 and n == 0:
                res.append(nums.copy())
            start = 0
            if not nums:
                start = 1
            else:
                start = nums[-1] + 1
            for i in range(start, 10):
                if i == 9 and k > 1 or i > n:
                    return
                nums.append(i)
                dfs(k - 1, n - i)
                nums.pop()

        dfs(k, n)
        return res

    def combinationSum31(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int, t: int):
            d = k - len(path)  # 还要选d个数
            if t < 0 or t > (i * 2 - d + 1) * d // 2:  # 剪枝
                return
            if d == 0:  # 找到一个合法组合
                ans.append(path.copy())
                return
            for j in range(i, d - 1, -1):  # 因为还要d个数，所以只能遍历从i到d-1的数字
                path.append(j)
                dfs(j - 1, t - j)
                path.pop()

        dfs(9, n)
        return ans

    # 选或不选
    def combinationSum32(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int, t: int):
            d = k - len(path)  # 还要选d个数
            if t < 0 or t > (i * 2 - d + 1) * d // 2:  # 剪枝
                return
            if d == 0:  # 找到一个合法组合
                ans.append(path.copy())
                return
            # 不选i
            if i > d:
                dfs(i - 1, t)
            # 选i
            path.append(i)
            dfs(i - 1, t - i)
            path.pop()

        dfs(9, n)
        return ans


Solution().combinationSum3(3, 9)
