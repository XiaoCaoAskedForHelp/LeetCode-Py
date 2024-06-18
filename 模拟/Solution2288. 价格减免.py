class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        nums = []
        sentence = ' ' + sentence + ' '
        n = len(sentence)
        start = 0
        while start < n - 1:
            if sentence[start] == ' ' and sentence[start + 1] == '$':
                end = start + 2
                flag = True
                while end < n and sentence[end] != ' ':
                    if sentence[end] > '9' or sentence[end] < '0':
                        flag = False
                    end += 1
                if flag and start + 2 < end:
                    num = int(sentence[start + 2: end])
                    nums.append((num * (1 - discount / 100), start + 2, end))
                start = end
            else:
                start += 1
        for i, (num, start, end) in enumerate(nums[::-1]):
            sentence = sentence[:start] + '%.2f' % num + sentence[end:]
        return sentence.strip()

    # 直接split处理
    def discountPrices1(self, sentence: str, discount: int) -> str:
        d = 1 - discount / 100
        a = sentence.split(' ')
        for i, w in enumerate(a):
            if w[0] == '$' and w[1:].isdigit():
                a[i] = f"${int(w[1:]) * d :.2f}"
        return ' '.join(a)


Solution().discountPrices(sentence="1 2 $3 4 $5 $6 7 8$ $9 $10$", discount=100)
