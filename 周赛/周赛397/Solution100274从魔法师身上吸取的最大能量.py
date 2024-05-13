from typing import List


class Solution:
    # 反向，遍历最后k个就行
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        res = max(energy[n - k:n])
        for i in range(n - 1, n - k - 1, -1):
            j = i
            tmp = energy[i]
            while j - k >= 0:
                j = j - k
                tmp += energy[j]
                res = max(res, tmp)
        return res


Solution().maximumEnergy(energy=[5, -10, 4, 3, 5, -9, 9, -7], k=2)
Solution().maximumEnergy(energy=[8, -5], k=1)
Solution().maximumEnergy(energy=[-2, -3, -1], k=2)
Solution().maximumEnergy(energy=[5, 2, -10, -5, 1], k=3)
