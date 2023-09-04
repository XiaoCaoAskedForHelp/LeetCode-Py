from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break

        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            # 如果起点或终点有障碍物，直接返回0
            return 0

        dp = [[0] * n for _ in range(m)]  # 创建一个二维列表用于存储路径数

        # 设置起点的路径数为1
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        # 计算第一列的路径数
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]

        # 计算第一行的路径数
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]

        # 计算其他位置的路径数
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]  # 返回终点的路径数

    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        dp = [0] * len(obstacleGrid[0])

        for j in range(len(dp)):
            if obstacleGrid[0][j] == 1:
                dp[j] = 0
            elif j == 0:
                dp[j] = 1
            else:
                dp[j] = dp[j - 1]

        # 计算其他行的路径数
        for i in range(1, len(obstacleGrid)):
            for j in range(len(dp)):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j != 0:
                    dp[j] = dp[j] + dp[j - 1]

        return dp[-1]

    def uniquePathsWithObstacles3(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * n  # 创建一个一维列表用于存储路径数

        # 初始化第一行的路径数
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[j] = 1

        # 计算其他行的路径数
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j - 1]

        return dp[-1]  # 返回最后一个元素，即终点的路径数

    def uniquePathsWithObstacles3(self, obstacleGrid):
        if obstacleGrid[0][0] == 1:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [0] * n  # 创建一个一维列表用于存储路径数

        # 初始化第一行的路径数
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[j] = 1

        # 计算其他行的路径数
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                    continue

                dp[j] += dp[j - 1]

        return dp[-1]