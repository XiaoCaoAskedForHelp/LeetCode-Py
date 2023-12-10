from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curSum = 0
        minFuel = float('inf')

        for i in range(len(gas)):
            rest = gas[i] - cost[i]
            curSum += rest
            if curSum < minFuel:
                minFuel = curSum

        if curSum < 0:
            return -1  # 情况1，总总油量<总消耗量是不可能到终点的
        if minFuel >= 0:
            return 0  # 情况2：从起点出发，油量一直处于>=0状态，说明从起点就可以正常绕一圈

        for i in range(len(gas) - 1, -1, -1):
            rest = gas[i] - cost[i]
            minFuel += rest
            if minFuel >= 0:
                return i  # 找到一个位置使得可以从该位置出发补全从o位置出发缺的油

        return -1

    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
        cur_sum = 0
        total_sum = 0
        start = 0
        for i in range(len(gas)):
            cur_sum += gas[i] - cost[i]
            total_sum += gas[i] - cost[i]

            if cur_sum < 0:
                start = i + 1
                cur_sum = 0

        if total_sum < 0:
            return -1
        return start
