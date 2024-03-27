t = int(input())


# 三个木块只有4,6,8这三种情况
# 如果三个都有一条边相等（同为长边或短边）或者两个矩形有一条边相等并且另一边之和等于另一个矩形一条边，那么结果为4
# 如果一个矩形两边和另外两矩形一边相等 或者 两矩形有一边相等 结果为6
# 如果上述情况都不成立则为8
def check4_1(a, b, c):
    if a == b == c:
        return True


def check4_2(a1, b1, a2, b2, a3, b3):
    for i in [a1, b1]:
        if i == a2 + a3 and b2 == b3:
            return True
        if i == a2 + b3 and b2 == a3:
            return True
        if i == b2 + a3 and a2 == b3:
            return True
        if i == b2 + b3 and a2 == a3:
            return True
    return False


def check6(a, b, c):
    if a + b == c or a + c == b or b + c == a:
        return True
    elif a == b or a == c or b == c:
        return True
    else:
        return False


for i in range(t):
    ans = 8
    s = list(map(int, input().split()))
    a1, b1, a2, b2, a3, b3 = s
    for i in range(0, 2):
        for j in range(2, 4):
            for k in range(4, 6):
                x1, x2, x3 = s[i], s[j], s[k]
                if check4_1(x1, x2, x3):
                    ans = min(4, ans)
                if check6(x1, x2, x3):
                    ans = min(6, ans)
    if check4_2(a1, b1, a2, b2, a3, b3) or check4_2(a3, b3, a1, b1, a2, b2) or check4_2(a2, b2, a1, b1, a3, b3):
        ans = min(4, ans)
    print(ans)
