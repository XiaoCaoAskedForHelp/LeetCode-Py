class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 因为字符串是不可变类型，所以反转单词的时候，需要将其转换成列表，然后通过join函数再将其转换成列表，所以空间复杂度不是O(1)
        # 删除前后空白
        # s = s.strip()
        # 反转整个字符串
        s = s[::-1]
        # 将字符串拆分为单词，并翻转每次单词, python的split默认分隔符是单个空格或者多个空格(including \\n \\r \\t \\f and spaces)
        s = ' '.join(word[::-1] for word in s.split())
        return s
        pass

    def reverseWords2(self, s):
        # 将字符串拆分为单词
        words = s.split()
        # 使用双指针翻转单词
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        # 将列表转换为字符串
        return " ".join(words)