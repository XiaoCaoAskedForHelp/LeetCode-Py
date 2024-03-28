from typing import List


class Solution:
    # 模拟   超时
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        mod = 10 ** 9 + 7
        visited = [0] * n
        cnt = 1  # 访问房间的个数
        ans = 0  # 访问的天数
        i = 0
        while cnt < n:
            visited[i] += 1
            if visited[i] % 2 == 1:
                i = nextVisit[i]
            else:
                i = (i + 1) % n
            ans = (ans + 1) % mod
            if not visited[i]:
                cnt += 1
        return ans

    # 刚到就只能回退，偶数次就可以进一
    # dp
    def firstDayBeenInAllRooms1(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [0] * n  # 走完第i个房间需要多少天
        i = 0
        mod = 10 ** 9 + 7
        while i < n - 1:
            if i == nextVisit[i]:  # 如果下标和前进的房间号相等，那就只需要走两次到偶数次就可以前进一步
                dp[i] = ((dp[i - 1] if i - 1 >= 0 else 0) + 2) % mod
            else:  # 下标比房间号小，那就需要回退将之前走的路在走一遍,等于原来走到这的天数+需要回退的天数
                dp[i] = (dp[i - 1] + dp[i - 1] - (dp[nextVisit[i] - 1] if nextVisit[i] - 1 >= 0 else 0) + 2) % mod
            i += 1
        return dp[-2]

    # 由于访问偶数次才能访问右边的下一个房间，所以对于 i 左边的房间，我们一定都访问了偶数次（不然不可能到达 i）
    # 那么当我们访问这个范围内的每个房间时，算上本次访问，访问次数一定是奇数，所以要想重新回到i，对于[j, i−1] 范围内的每个房间，我们都需要执行一次「回访」。
    # 定义 f[i] 表示从「访问到房间 i 且次数为奇数」到「访问到房间 i 且次数为偶数」所需要的天数。
    def firstDayBeenInAllRooms2(self, nextVisit: List[int]) -> int:
        s = [0] * len(nextVisit)  # s是前缀和，第一个是0，表示到达房间i之前所用天数
        for i, j in enumerate(nextVisit[:-1]):
            s[i + 1] = (s[i] * 2 - s[j] + 2) % 1_000_000_007
        return s[-1]


Solution().firstDayBeenInAllRooms1(nextVisit=[0, 0, 2])
Solution().firstDayBeenInAllRooms1(nextVisit=[0, 1, 2, 0])
