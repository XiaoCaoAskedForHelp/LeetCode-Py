from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        dic = Counter(tasks)
        res = 0
        for _, cnt in dic.items():
            if cnt == 1:
                return -1
            res += (cnt // 3 + 1 if cnt % 3 != 0 else cnt // 3)  # 只要不是1的都能变为2x + 3y的形式
        return res

    def minimumRounds1(self, tasks: List[int]) -> int:
        cnt = Counter(tasks)
        if 1 in cnt.values():
            return -1
        return sum((c + 2) // 3 for c in cnt.values())
