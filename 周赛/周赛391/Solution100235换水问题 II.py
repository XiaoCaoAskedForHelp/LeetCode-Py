class Solution:
    # 贪心
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = 0
        res += numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange
            numExchange += 1
            numBottles += 1
            res += 1
        return res
