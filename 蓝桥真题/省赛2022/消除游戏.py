s = "#" + input() + "#"
N = 10 ** 6 + 10
l, r = [0] * N, [0] * N  # 初始化左右指针
# 满足题目中的说的边缘边缘字符，需要和你左右两边的字符进行比较，然后记录删除的位置
# 所以直接使用两个数字构造两个数组记录左右位置，然后删除的话也只需要通过将左右位置进行变换，就可以进行软删除，这种思想非常神奇
for i in range(1, len(s) - 1):
    l[i] = i - 1
    r[i] = i + 1
pos = []  # 储存边缘字符的位置
exist = [True] * N  # 字符串该位置是否存在


# 检查边缘字符
def check(index):  # 检查字符串是否存在边缘字符
    if s[l[index]] == "#" or s[r[index]] == "#":
        return
    elif s[l[index]] != s[index] and s[r[index]] == s[index]:
        pos.append(l[index])
        pos.append(index)
    elif s[r[index]] != s[index] and s[l[index]] == s[index]:
        pos.append(index)
        pos.append(r[index])


def remove(index):  # 删除index这个字符  x index j 将x的右边变为j的下标，将j的左边变为x的下标
    if exist[index]:
        r[l[index]] = r[index]
        l[r[index]] = l[index]
        exist[index] = False


# 第一次计算边缘字符的位置
for i in range(1, len(s) - 1):
    check(i)
while pos:
    newpos = set()  # 存储还没有被删除的位置
    for i in pos:
        if not exist[i]:
            continue
        remove(i)
        newpos.add(l[i])  # 存储北山元素的左右指针
        newpos.add(r[i])
    pos = []  # 将上一轮边缘字符删除
    for i in newpos:
        if exist[i]:
            check(i)  # pos又会被填充需要删除的字符
ans = ""
for i in range(1, len(s) - 1):
    if exist[i]:
        ans += s[i]
print(ans if ans != "" else "EMPTY")
