class Solution(object):
    def reverseLeftWords(self, s: str, n: int) -> str:
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        return s[n:] + s[0:n]

    # 将不可变的字符串变为可变的列表进行翻转，然后进行拼接
    def reverseLeftWords1(self, s: str, n: int) -> str:
        s = list(s)
        s[0:n] = list(reversed(s[0:n]))
        s[n:] = list(reversed(s[n:]))
        s.reverse()
        return "".join(s)

    def reverseLeftWords1(self, s: str, n: int) -> str:
        l = len(s)
        # 复制输入字符串与它自己连接
        s = s + s
        return s[n:n + l]
