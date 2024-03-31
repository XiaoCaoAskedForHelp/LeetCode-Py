class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        tmp = 0
        num = x
        while x:
            tmp += (x % 10)
            x //= 10
        if num % tmp == 0:
            return tmp
        return -1

Solution().sumOfTheDigitsOfHarshadNumber(18)