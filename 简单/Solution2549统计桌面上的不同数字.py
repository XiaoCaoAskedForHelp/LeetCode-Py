class Solution:
    def distinctIntegers(self, n: int) -> int:
        st = set([n])

        visited = [False] * (n + 1)
        queue = [n]
        while queue:
            num = queue.pop()
            for i in range(2, num):
                if not visited[num] and num % i == 1:
                    queue.append(i)
                    st.add(i)
            visited[num] = True

        return len(st)

    # 模拟每天的变化
    def distinctIntegers1(self, n: int) -> int:
        nums = [0] * (n + 1)
        nums[n] = 1
        for _ in range(1, n + 1):  # 最多就是n个数都出现了，所以就是n次
            for x in range(1, n + 1):
                if nums[x] == 0:
                    continue
                for i in range(1, n + 1):
                    if x % i == 1:
                        nums[i] = 1
        return sum(nums)

    def distinctIntegers(self, n: int) -> int:
        return 1 if n == 1 else n - 1


Solution().distinctIntegers(5)
