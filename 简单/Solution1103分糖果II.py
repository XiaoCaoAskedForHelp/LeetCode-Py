import bisect
from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        idx = 0
        candy = 1
        while candies:
            res[idx] += min(candy, candies)
            idx = (idx + 1) % num_people
            candies -= min(candy, candies)
            candy += 1
        return res

    def distributeCandies1(self, candies: int, num_people: int) -> List[int]:
        p = int((2 * candies + 0.25) ** 0.5 - 0.5)  # 一共完整的分发的多少轮
        remain = int(candies - p * (p + 1) * 0.5)
        rows, cols = p // num_people, p % num_people
        res = [0] * num_people
        for i in range(num_people):
            # 完整的
            res[i] = (i + 1 + i + 1 + (rows - 1) * num_people) * rows // 2
            if i < cols:
                res[i] += i + 1 + rows * num_people
        res[cols] += remain
        return res


Solution().distributeCandies1(candies=10, num_people=3)
Solution().distributeCandies1(candies=7, num_people=4)
