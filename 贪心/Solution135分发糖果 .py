from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        cnt = [1] * len(ratings)

        # 从前往后遍历，处理右侧比左侧评分高的情况
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                cnt[i] = max(cnt[i], cnt[i - 1] + 1)

        # 从后往前遍历，处理左侧比右侧评分高的情况
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                cnt[i] = max(cnt[i], cnt[i + 1] + 1)

        return sum(cnt)
