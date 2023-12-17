class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # 将整数转换为字符串
        strNum = str(n)
        # flag用来标记赋值9从哪里开始
        # 设置为字符串长度，为了防止第二个for循环在flag没有被赋值的情况下执行
        flag = len(strNum)

        # 从右往左遍历字符串
        for i in range(len(strNum) - 1, 0, -1):
            # 如果当前字符比前一个字符小，说明需要修改前一个字符
            if strNum[i - 1] > strNum[i]:
                flag = i  # 更新flag的值，记录需要修改的位置
                # 将前一个字符减1，以保证递增性质
                strNum = strNum[:i - 1] + str(int(strNum[i - 1]) - 1) + strNum[i:]

        # 将flag位置及之后的字符都修改为9，以保证最大的递增数字
        for i in range(flag, len(strNum)):
            strNum = strNum[:i] + '9' + strNum[i + 1:]

        return int(strNum)

    def monotoneIncreasingDigits1(self, N: int) -> int:
        # 将整数转换为字符串
        strNum = list(str(N))

        # 从右往左遍历字符串
        for i in range(len(strNum) - 1, 0, -1):
            # 如果当前字符比前一个字符小，说明需要修改前一个字符
            if strNum[i - 1] > strNum[i]:
                strNum[i - 1] = str(int(strNum[i - 1]) - 1)  # 将前一个字符减1
                # 将修改位置后面的字符都设置为9，因为修改前一个字符可能破坏了递增性质
                # for j in range(i, len(strNum)):
                #     strNum[j] = '9'
                strNum[i:] = '9' * (len(strNum) - i)

        # 将列表转换为字符串，并将字符串转换为整数并返回
        return int(''.join(strNum))

    def monotoneIncreasingDigits(self, n: int) -> int:
        strNum = str(n)
        for i in range(len(strNum) - 1,0,-1):
            # 如果当前字符比前一个字符小，说明需要修改前一个字符
            if strNum[i - 1] > strNum[i]:
                # 将前一个字符减1，以保证递增性质
                # 使用字符串切片操作将修改后的前面部分与后面部分进行拼接
                strNum = strNum[:i - 1] + str(int(strNum[i - 1]) - 1) + '9' * (len(strNum) - i)
        return int(strNum)

