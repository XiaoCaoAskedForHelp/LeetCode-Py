class Solution:
    def minimumChairs(self, s: str) -> int:
        res = 0
        cnt = 0
        for c in s:
            if c == 'E':
                cnt += 1
                res = max(res, cnt)
            else:
                cnt -= 1
        return res