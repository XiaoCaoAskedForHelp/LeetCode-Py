import math
from cmath import inf

# 这个代码有问题
def quadrant(x, y):
    if x >= 0 and y > 0:
        return 1  # y的正半轴放在第一象限
    if x > 0 and y <= 0:
        return 2  # x的正半轴放在第二象限
    if x <= 0 and y < 0:
        return 3  # y的负半轴放在第三象限
    return 4


def tancmp(x, y):
    t = math.atan(abs(y) / abs(x)) if x != 0 else 10 ** 9
    if quadrant(x, y) in [1, 3]:
        return -1 * t
    else:
        return t


MAXN = 2 * 10 ** 5 + 5
dis = [0] * (MAXN << 2)


def push_up(p):
    dis[p] = min(dis[p << 1], dis[p << 1 | 1])


# 利用线段树维护每个点到原点的距离,要找的是下一个小于等于L^2的点，因此维护最小值。
def build(p: int, l: int, r: int):  # p是节点的序号
    if l == r:
        x, y, z, i = points[l]
        dis[p] = x * x + y * y
        return
    mid = (l + r) >> 1  # 二分构造
    build(p << 1, l, mid)  # 构造左分支
    build(p << 1 | 1, mid + 1, r)  # 构造右分支
    push_up(p)


def update(p: int, l: int, r: int, x: int, val):
    if l == r:
        dis[p] = val
        return
    mid = (l + r) >> 1
    if x <= mid:
        update(p << 1, l, mid, x, val)
    else:
        update(p << 1 | 1, mid + 1, r, x, val)
    push_up(p)  # 更新一下有变化的部分线段树


# ll,rr是树上的区间，l，r是要查询的区间
# 找右边第一个小于等于z^2的数字
def query(p: int, l: int, r: int, ll: int, rr: int, z: int):
    global idx
    if ll > rr:
        return False
    if l == r:
        idx = l
        return dis[p] <= z
    mid = (l + r) >> 1
    if ll <= mid:
        if dis[p << 1] <= z and query(p << 1, l, mid, ll, rr, z):  # 当左节点的值<=z时，就可以在左子树中搜索
            return True
    if rr > mid:
        if dis[p << 1 | 1] <= z and query(p << 1 | 1, mid + 1, r, ll, rr, z):
            return True
    return False


n, l = map(int, input().split())
# 首先进行角排序，按照顺时针排序，在利用线段树维护每个点到原点的距离xi平方+ yi平方
points = []
for i in range(1, n + 1):
    x, y, z = map(int, input().split())
    points.append((x, y, z, i))  # 记录i是为了方便记录和输出
# 先按象限进行排序，在按叉积值进行排序
points = [0] + sorted(points, key=lambda a: (quadrant(a[0], a[1]), tancmp(a[0], a[1])))
build(1, 1, n)

cnt = 0  # 记录是第几个碰到的
idx = 0  # 记录现在这个点的下标
last = 0  # 记录上一个点的下标
lastcnt = 0  # 记录上一个点是第几个碰到的
ans = [-1] * MAXN
while True:
    ok = query(1, 1, n, last + 1, n, l * l)  # [last + 1,n]这个区间去寻找去找第一个能被扫描到的点
    if ok:
        l = l + points[idx][2]  # 找到了点，距离增加
    else:
        ok = query(1, 1, n, 1, last - 1, l * l)  # [1, last - 1]这个区间去寻找去找第一个能被扫描到的点
        if ok:
            l = l + points[idx][2]  # 找到了点，距离增加
        else:  # 如果转了一圈还是没有找到点，直接break
            break
    update(1, 1, n, idx, inf)
    if last:
        # 如果现在这个点跟之前点在同一直线上
        if quadrant(points[last][0], points[last][1]) == quadrant(points[idx][0], points[idx][1]) \
                and tancmp(points[last][0], points[last][1]) == tancmp(points[idx][0], points[idx][1]):
            ans[points[idx][3]] = lastcnt
            cnt += 1
        else:
            cnt += 1
            ans[points[idx][3]] = cnt
            lastcnt = cnt
    else:
        cnt += 1
        ans[points[idx][3]] = cnt
        lastcnt = cnt
    last = idx
for i in range(1, n + 1):
    print(ans[i], end=" ")
