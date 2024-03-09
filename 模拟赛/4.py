# 求 12345678901234567890123456789012345678901234567890 除以 2023 的余数。

numstr = "12345678901234567890123456789012345678901234567890"
n = len(numstr)
tmp = 0
for i in range(0, n, 10):
    num = int(str.join('', [numstr[i] for i in range(i, i + 10)]))
    num = tmp * 10 ** 10 + num
    tmp = num % 2023
    print(tmp)

