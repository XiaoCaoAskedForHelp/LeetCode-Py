import math
from typing import List


# 贪心，从下到上，每一层兄弟节点的cost应该要相同，这样才能保证到他们两的路径相同
# 当叶节点都无需进行操作。我们就可以将它们全部移除。为了使得路径值保持不变，我们可以将叶节点的值增加至它们的双亲节点。
# 这样一来，所有的双亲节点都变成了新的叶节点，我们重复进行上述操作即可。当只剩一个节点（根节点）时，就可以得到最终的答案。

class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        # 计算满二叉树层数
        res = 0
        for i in range(n - 2, 0, -2):
            res += abs(cost[i] - cost[i + 1])
            # 叶子节点i和i+1的双亲节点下标为i//2
            cost[i // 2] += max(cost[i], cost[i + 1])  # 更新父节点，相当于把他变为了叶子节点

        return res

    def minIncrements1(self, n: int, cost: List[int]) -> int:
        def dfs(i):
            if 2 * i > n:
                return cost[i - 1]

            left_path = dfs(2 * i)
            right_path = dfs(2 * i + 1)
            self.res += abs(left_path - right_path)
            return cost[i - 1] + max(left_path, right_path)

        self.res = 0
        dfs(1)
        return self.res


Solution().minIncrements(7, [1, 5, 2, 2, 3, 3, 1])
