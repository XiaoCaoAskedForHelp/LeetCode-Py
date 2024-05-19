from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        odd = True
        for i, num in enumerate(nums):
            if i == 0:
                if num % 2:
                    odd = True
                else:
                    odd = False
            else:
                if (num % 2 and odd) or (num % 2 == 0 and not odd):
                    return False
                odd = num % 2 == 1
        return True


print(Solution().isArraySpecial(nums=[2, 1, 4]))
print(Solution().isArraySpecial(nums=[4, 3, 1, 6]))
