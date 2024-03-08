from functools import cache
from typing import List, Tuple


class Solution:

    # 超出时间限制
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # @cache   #使用缓存装饰器@functools.lru_cache(maxsize = None)缓存中间结果可以加快递归运行速度，但如果递归对象是list，则会报错unhashable type: 'list'
        def dfs(cnt: int, points: List[int], k: int):
            if cnt >= k:
                return 0
            n1 = dfs(cnt + 1, points[:-1], k) + points[-1]
            n2 = dfs(cnt + 1, points[1:], k) + points[0]
            return max(n1, n2)

        return dfs(0, cardPoints, k)

    # 超出内存限制
    def maxScore1(self, cardPoints: List[int], k: int) -> int:
        @cache
        def dfs(cnt: int, points: Tuple[int], k: int):
            if cnt >= k:
                return 0
            n1 = dfs(cnt + 1, points[:-1], k) + points[-1]
            n2 = dfs(cnt + 1, points[1:], k) + points[0]
            return max(n1, n2)

        points = tuple(cardPoints)
        return dfs(0, points, k)

    # 逆向思维,求两边最大的就是求中间最小的
    def maxScore2(self, cardPoints: List[int], k: int) -> int:
        mid = sum(cardPoints[i] for i in range(len(cardPoints) - k))
        tmp = mid
        for i in range(k):
            tmp = tmp - cardPoints[i] + cardPoints[i + len(cardPoints) - k]
            mid = min(tmp, mid)
        return sum(cardPoints) - mid

    # 与上面思想一样
    def maxScore3(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        m = n - k
        min_s = s = sum(cardPoints[:m])
        for i in range(m, n):
            s += cardPoints[i] - cardPoints[i - m]
            min_s = min(min_s, s)
        return sum(cardPoints) - min_s

    # 正向思维
    def maxScore4(self, cardPoints: List[int], k: int) -> int:
        ans = s = sum(cardPoints[:k])
        for i in range(1, k + 1):
            s += cardPoints[-i] - cardPoints[k - i]
            ans = max(s, ans)
        return ans


Solution().maxScore2(cardPoints=[1, 2, 3, 4, 5, 6, 1], k=3)
