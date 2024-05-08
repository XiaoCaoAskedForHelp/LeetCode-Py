from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 0
        sums = 0
        for i in range(len(plants)):
            plant = plants[i]
            sums += plant
            if sums > capacity:
                res += i * 2
                sums = plant
        return res + len(plants)

    def wateringPlants1(self, plants: List[int], capacity: int) -> int:
        ans = len(plants)
        water = capacity
        for i, need in enumerate(plants):
            if water < need:
                ans += i * 2
                water = capacity
            water -= need
        return ans


Solution().wateringPlants(plants=[2, 2, 3, 3], capacity=5)
