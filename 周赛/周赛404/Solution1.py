class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        s1 = 0
        s2 = 0
        redf = 0
        redb = 0
        for i in range(1, 100, 2):
            s1 += i
            if s1 > red:
                redf = i - 2
                break
        for i in range(2, 100, 2):
            s2 += i
            if s2 > red:
                redb = i - 2
                break
        s1 = 0
        s2 = 0
        bluef = 0
        blueb = 0
        for i in range(1, 100, 2):
            s1 += i
            if s1 > blue:
                bluef = i - 2
                break
        for i in range(2, 100, 2):
            s2 += i
            if s2 > blue:
                blueb = i - 2
                break

        return max(max(redf, blueb) if abs(redf - blueb) <= 1 else min(redf, blueb) + 1,
                   max(redb, bluef) if abs(redb - bluef) <= 1 else min(redb, bluef) + 1)


Solution().maxHeightOfTriangle(10, 1)
