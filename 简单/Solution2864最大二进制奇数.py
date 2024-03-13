class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = 0
        for i in s:
            if i == '1':
                cnt += 1
        n = len(s)
        res = '1' * (cnt - 1) + '0' * (n - cnt) + '1'
        return res

    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = s.count('1')
        return '1' * (cnt - 1) + '0' * (len(s) - cnt) + '1'


Solution().maximumOddBinaryNumber("0101")
