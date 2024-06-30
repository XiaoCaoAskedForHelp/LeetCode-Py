from typing import List

# (sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        # 子序列奇数项余数相同，偶数项相同
        # 维护一个二维数据，表示最后两项模k分别为y和x的子序列长度
        f = [[0] * k for _ in range(k)]
        for x in nums:
            x %= k
            for y, fxy in enumerate(f[x]):  # x的余数要和前两位的数的余数相同
                f[y][x] = fxy + 1
        return max(map(max, f))
