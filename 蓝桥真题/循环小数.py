p, q = map(int, input().split())
s = input()


# 小于一的循环小数，分子小于分母
# 纯循环小数转化位分数，就等于循环体部分除以与循环体位数相同的9

# 0.114285742857= 0.11 + 0.42857
# = 11/100 + 42857/9999900 = 11*99999 + 42857 / 9999900

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


m = int(s[:p - 1] if s[:p - 1] else 0)
n = int(s[p - 1:])
lm = p - 1
ln = q - p + 1
fenzi = m * (10 ** ln - 1) + n
fenmu = 10 ** q - 10 ** lm
yinzi = gcd(fenzi, fenmu)
print(fenzi // yinzi, fenmu // yinzi)
