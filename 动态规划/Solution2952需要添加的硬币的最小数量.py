from typing import List


class Solution:
    # 假设现在得到了区间[0, s−1] 中的所有整数,如果此时遍历到整数 x=coins[i]，那么把 [0,s−1] 中的每个整数都增加 x，我们就得到了区间 [x,s+x−1] 中的所有整数。看着中间有没有数字漏掉
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        ans, s, i = 0, 1, 0  # 表示s之前的数字都已经拿到了
        while s <= target:
            if i < len(coins) and coins[i] <= s:  # 如果硬币大小比s小，那原本的[0,s-1]加上[coin,s-1+coin]是能连上的，中间不会有漏的数字
                s += coins[i]
                i += 1
            else:  # 如果加硬币发现直接大于s，证明s这个数没法用coins加起来得到
                s *= 2  # 所以加上s，[0,s-1] 就会多加一段[s,2s-1],说明2s之前的数就都得到了
                ans += 1
        return ans

Solution().minimumAddedCoins(coins=[1, 1, 1], target=20)
