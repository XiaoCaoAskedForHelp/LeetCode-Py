from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        tmp = 0
        for i in range(0, abs(k)):
            tmp += code[i]
        res = [0] * n
        if k > 0:
            right = tmp
            for i in range(n):
                right = right - code[(i + n) % n] + code[(i + k + n) % n]
                res[i] = right
        else:
            left = tmp
            k = -k
            for i in range(n):
                left = left - code[(i + n) % n] + code[(i + k + n) % n]
                res[(i + k + n + 1) % n] = left
        return res

    # 滑动窗口，三种情况一起处理。
    # k>0，第一个窗口的的下标范围为 [1,k+1)。
    # k<0，第一个窗口的的下标范围为 [n−∣k∣,n)。
    def decrypt1(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        r = k + 1 if k > 0 else n  # 确定右端点
        k = abs(k)
        s = sum(code[r - k:r])
        for i in range(n):
            ans[i] = s
            s += code[r % n] - code[(r - k) % n]  # 加上右端点，减去左端点
            # r += 1
            r = (r + 1) % n  # r这个对n求余加不加都可以，因为滑动窗口计算的时候有求余
        return ans

    # 前缀和
    def decrypt2(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans
        sum = [0] * (2 * n + 10)
        for i in range(1, 2 * n + 1):
            sum[i] = sum[i - 1] + code[(i - 1) % n]
        for i in range(1, n + 1):
            ans[i - 1] = sum[i + n - 1] - sum[i + n + k - 1] if k < 0 else sum[i + k] - sum[i]
        return ans


Solution().decrypt(code=
                   [10, 5, 7, 7, 3, 2, 10, 3, 6, 9, 1, 6], k=-4)
