# 若没有油箱的限制，仅用优先队列即可。将所有加油站扔到堆里，贪心得在油价最少的加油站加油。
import heapq


# 但若有限制，在一个加油站加油后，之后到达的加油站的到达油量也要更新，能加的油量也要更新，故采用线段树or树状数组维护区间到达加油站的油量的最大值。

# 怎么判断当前是最低花费且能够到达终点？
# 1.首先最直接的方法，每到达一个地方我都加满油，这样还到不了那说明这把G了
# 2.在1的前提下，我想要知道最低的话，就得有个mincost记录花费，有个DFS全部尝试一遍

# i 表示当前节点的索引，l 和 r 分别表示当前节点对应的区间的左右边界。
# 如果当前节点表示的是叶子节点（即 l == r），则将 rest[i] 初始化为 0，表示到达该加油站时车辆的剩余可加油量。
# 否则，递归构建左右子节点，然后更新当前节点的值。
def build(i: int, l: int, r: int):
    if l == r:
        rest[i] = 0  # 初识时每个区间内的可加油量都是0
        return
    mid = (l + r) // 2
    build(i << 1, l, mid)
    build(i << 1 | 1, mid + 1, r)
    rest[i] = max(rest[i << 1], rest[i << 1 | 1])


# 向线段树中的某个区间 [ll, rr] 添加油量 v 的操作
# i: 当前线段树节点的索引。
# l 和 r: 当前节点所代表的区间范围 [l, r]。
# ll 和 rr: 要添加油量的目标区间 [ll, rr]。
# v: 要添加的油量。
def add(i: int, l: int, r: int, ll: int, rr: int, v: int):
    if ll <= l and rr >= r:
        rest[i] += v
        k[i] += v
        return
    pd(i)
    mid = (l + r) // 2
    if mid >= ll:
        add(i << 1, l, mid, ll, rr, v)
    if mid < rr:
        add(i << 1 | 1, mid + 1, r, ll, rr, v)


def pd(i: int):
    if k[i] != 0:
        k[i << 1] += k[i]
        k[i << 1 | 1] += k[i]
        rest[i << 1] += k[i]
        rest[i << 1 | 1] += k[i]
        k[i] = 0


# l 和 r: 当前节点所代表的区间范围 [l, r]。
# ll 和 rr: 要查询油量的目标区间 [ll, rr]。
def query(i: int, l: int, r: int, ll: int, rr: int):
    if ll <= l and r <= rr:
        return rest[i]
    pd(i)
    res = 0
    mid = (l + r) // 2
    if mid >= ll:
        res = max(res, query(i << 1, l, mid, ll, rr))
    if mid < rr:
        res = max(res, query(i << 1 | 1, mid + 1, r, ll, rr))
    rest[i] = max(rest[i << 1], rest[i << 1 | 1])
    return res


# rest[]：表示了在某一段距离内车辆能够剩余的最大可加油量。通过这个值，可以知道当前节点区间内车辆剩余的最大可加油量，进而确定是否需要在该区间内加油，以及加多少油。
# k[]：用于延迟更新当前节点和其子节点的加油量。由于需要在每个加油站进行计算和决策，而每个加油站都会影响到其所在的区间内的剩余可加油量，因此通过延迟更新可以确保在需要计算时，区间内的剩余可加油量是最新的。

if __name__ == '__main__':
    n, m = map(int, input().split())
    vol = m
    maxn = 2 * 10 ** 5 + 5
    rest = [0] * (maxn << 2)  # 区间内剩余油量
    k = [0] * (maxn << 2)  # 记录了当前节点所表示的区间内的需要延迟更新的加油量。
    dis = [0]  # 加油站的距离
    cost = [0]  # 加油成本
    lim = [0]  # 剩余可加油量
    ans = 0
    for i in range(n):
        d, c, l = list(map(int, input().split()))
        dis.append(d)
        cost.append(c)
        lim.append(l)
    build(1, 1, n)
    queue = []
    for i in range(1, n + 1):
        vol -= dis[i]  # 剩余的油量
        # 当前车辆的剩余可加油量小于0时，需要加油
        while vol < 0:
            # 如果优先队列为空，则无法加油，输出-1
            if not queue:
                print(-1)
                exit()
            c, idx = heapq.heappop(queue)  # 从优先队列中取出成本最小的加油站
            # 计算当前加油站可加油的最大值，考虑剩余油量和该加油站的可加油量的最小值
            cnt = min(m - query(1, 1, n, idx, i - 1), lim[idx])
            # 如果可加油量为负数，则跳过当前加油站
            if cnt <= 0:
                continue

            # 如果可加油量小于剩余油量
            if cnt <= -vol:
                ans += c * cnt  # 计算加油成本
                vol += cnt  # 更新剩余油量
                lim[idx] = 0  # 将该加油站的可加油量置为0
                add(1, 1, n, idx, i - 1, cnt)  # 更新线段树信息，表示在当前加油站加了cnt的油
            else:
                ans += c * (-vol)  # 计算加油成本
                lim[idx] = cnt + vol  # 更新该加油站的可加油量
                add(1, 1, n, idx, i - 1, -vol)  # 更新线段树信息，表示在当前加油站加油-vol的油
                heapq.heappush(queue, (c, idx))  # 将当前加油站重新加入优先队列
                vol = 0  # 更新剩余油量为0

        # 如果剩余可加油量大于0，则可在当前加油站加油
        if vol > 0:
            add(1, 1, n, i, i, vol)

        # 更新当前加油站的可加油量，考虑当前剩余油量和车辆的可加油量的最小值
        lim[i] = min(lim[i], m - vol)

        # 将当前加油站加入优先队列
        heapq.heappush(queue, (cost[i], i))
    print(ans)
