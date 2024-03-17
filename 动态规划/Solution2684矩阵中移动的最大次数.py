from collections import deque
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        for j in range(n - 2, -1, -1):
            for i in range(m):
                if i - 1 >= 0 and grid[i][j] < grid[i - 1][j + 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j + 1] + 1)
                if grid[i][j] < grid[i][j + 1]:
                    dp[i][j] = max(dp[i][j], dp[i][j + 1] + 1)
                if i + 1 < m and grid[i][j] < grid[i + 1][j + 1]:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j + 1] + 1)
        return max([dp[i][0] for i in range(m)])

    # 超出时间限制，感觉是pop等操作耗时
    def maxMoves1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque(range(m))
        for j in range(1, n):
            l = len(q)
            while l:
                i = q.popleft()
                for i2 in [i - 1, i, i + 1]:
                    if 0 <= i2 < m and grid[i][j - 1] < grid[i2][j]:
                        q.append(i2)
                l -= 1
            if not q:
                return j - 1
        return n - 1

    def maxMoves2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = set(range(m))
        for j in range(1, n):
            q2 = set()
            for i in q:
                for i2 in [i - 1, i, i + 1]:
                    if 0 <= i2 < m and grid[i][j - 1] < grid[i2][j]:
                        q2.add(i2)
            q = q2
            if not q:
                return j - 1
        return n - 1


Solution().maxMoves(grid=
                    [[1000000, 92910, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033,
                      1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049,
                      1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065,
                      1066, 1067, 1068],
                     [1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084,
                      1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100,
                      1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116,
                      1117, 1118]])
Solution().maxMoves(grid=[[2, 4, 3, 5], [5, 4, 9, 3], [3, 4, 2, 11], [10, 9, 13, 15]])
