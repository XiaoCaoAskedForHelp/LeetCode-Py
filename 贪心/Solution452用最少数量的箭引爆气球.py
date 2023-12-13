from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0: return 0
        points.sort(key=lambda x: x[0])
        result = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]:  # 气球i和气球i-1不挨着，注意这里不是>=
                result += 1
            else:
                points[i][1] = min(points[i - 1][1], points[i][1])  # 更新重叠气球最小右边界
        return result

    def findMinArrowShots1(self, points: List[List[int]]) -> int:
        points.sort(key=(lambda x: x[0]))
        sl, sr = points[0][0], points[0][1]
        count = 1
        for i in points:
            if i[0] > sr:
                count += 1
                sl, sr = i[0], i[1]
            else:
                sl = max(sl, i[0])
                sr = min(sr, i[1])
        return count
