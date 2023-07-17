class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = list()
        for item in s:
            if res and res[-1] == item:
                res.pop()
            else:
                res.append(item)
        return "".join(res)

    # 使用双指针模拟栈
    def removeDuplicates1(self, s: str) -> str:
        res = list(s)
        slow = fast = 0
        length = len(s)

        while fast < length:
            # fast用来遍历字符串，slow指针用来不重复的字符串
            res[slow] = res[fast]

            # 如果发现和前一个一样，就退一格指针
            if slow > 0 and res[slow] == res[slow - 1]:
                slow -= 1
            else:
                slow += 1
            fast += 1
        return "".join(res[0: slow])


Solution().removeDuplicates1("abbaca")
