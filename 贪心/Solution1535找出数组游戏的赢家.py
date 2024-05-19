from typing import List


class Solution:
    # 贪心，要跟前面的最大的一个比，然后在尽可能的比后面的数字大，然后满足k就行，
    # 如果一个数字能比他后面的所有数字都大，那结果肯定是它
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n - 1:
            return max(arr)
        m = -1
        end = -1
        for i in range(n):
            if i == 0:
                end = max(end, i + 1)
                while end < n and arr[0] > arr[end]:
                    end += 1
                m = arr[0]
                if end != n:
                    if end - i - 1 >= k:
                        return arr[0]
                else:
                    return arr[0]
            else:
                if arr[i] > m:
                    end = max(end, i + 1)
                    while end < n and arr[i] > arr[end]:
                        end += 1
                    m = max(arr[i], m)
                    if end != n:
                        if end - i - 1 + 1 >= k:
                            return arr[i]
                    else:
                        return arr[i]
        return -1

    # 考察游戏执行的流程，本质上是在从左到右遍历 arr，求数组最大值（打擂台）。我们要找首个连续 k 回合都是最大值的数。
    # 示例 1 的 arr=[2,1,3,5,4,6,7],k=2，从左到右遍历的过程中，历史最大值依次为 2,3,5,6,7，其中元素 5 是首个连续 k 回合都是最大值的数。
    # 如果遍历完 arr 也没找到这样的数，那么答案就是 arr 的最大值 mx，因为此时比 mx 小的数都会移到 mx 的右边，所以后面比大小都是 mx 胜利。

    def getWinner1(self, arr: List[int], k: int) -> int:
        mx = arr[0]
        win = -1  # 对于arr[0] 来说，需要连续k + 1个回合都是最大值
        for x in arr:
            if x > mx:  # 新的最大值
                mx = x  # 记录历史最大值，然后从这个数开始比较，所以win次数变为0
                win = 0
            win += 1  # 获胜回合+1
            if win == k:
                break
        return mx  # 直接返回满足条件的历史最大值


Solution().getWinner1(arr=[2, 1, 3, 5, 4, 6, 7], k=2)
