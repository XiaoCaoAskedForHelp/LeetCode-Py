n, m = map(int, input().split())

w = [0] + list(map(int, input().split()))  # r[i] 表示第i天可以用于租借的教室数量
d = [0]  # 租借的教室数量
s = [0]  # 租借开始
t = [0]  # 租借结束
for i in range(m):
    d1, s1, t1 = map(int, input().split())
    d.append(d1)
    s.append(s1)
    t.append(t1)


# 判断mid是否符合能租借的要求，满足返回true
def check(mid):
    b = [0] * (n + 2)  # 差分数组将复杂度降为O（m+n）,初始化为O相当于就是完成了差分数组
    for i in range(1, mid + 1):
        b[s[i]] += d[i]
        b[t[i] + 1] -= d[i]
    for i in range(1, n + 1):
        b[i] += b[i - 1]
        if b[i] > w[i]:
            return False
    return True


l, r = 0, m

while l < r:
    mid = l + r + 1 >> 1  # +1是为什么防止死循环
    if (check(mid)):
        l = mid  # 说明mid这个地方也是满足的，l只需要到mid就行
    else:
        r = mid - 1  # mid这个地方不满足，所以至少要减一才能满足

if l == m:
    print(0)
else:
    print(-1)
    print(l + 1)
