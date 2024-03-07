from typing import List


class Solution:
    # 超时
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = [0] * len(word)
        num = 0
        for i in range(len(word)):
            num = num * 10 + int(word[i])
            if num % m == 0:
                res[i] = 1
        return res

    # (a*10 + b) mod m = (a mod m * 10 + b) mod m
    # 看来越大的数字进行%运算耗费的时间越多
    def divisibilityArray1(self, word: str, m: int) -> List[int]:
        res = [0] * len(word)
        num = 0
        for i in range(len(word)):
            # num = (num * 10 + int(word[i])) % m
            num = (num * 10 + ord(word[i]) - ord('0')) % m
            if num % m == 0:
                res[i] = 1
        return res


Solution().divisibilityArray("998244353", 3)
