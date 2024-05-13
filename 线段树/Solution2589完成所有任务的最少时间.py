from typing import List


class Solution:
    # 贪心
    # 按照区间右端点从小到大排序
    # 尽可能把区间安装在区间的后面，这样下一个区间就能统计到更多以运行的时间点
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[1])
        run = [False] * (tasks[-1][1] + 1)  # 最多的运行时间就是最后一个任务的end时间
        for start, end, d in tasks:
            d -= sum(run[start:end + 1])  # 去掉运行中的时间点
            if d <= 0:  # 该任务已经完成
                continue
            # 该任务尚未完成，从后往前找没有运行的时间点
            for i in range(end, start - 1, -1):
                if run[i]:  # 已运行
                    continue
                run[i] = True  # 运行
                d -= 1
                if d == 0:
                    break
        return sum(run)

    def findMinimumTime1(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[1])
        u = tasks[-1][1]
        m = u * 4
        cnt = [0] * m
        todo = [False] * m  # lazy tag

        def do(o: int, l: int, r: int):
            cnt[o] = r - l + 1
            todo[o] = True

        def pushdown(o: int, l: int, m: int, r: int):
            if todo[o]:
                todo[o] = False
                do(o * 2, l, m)
                do(o * 2 + 1, m + 1, r)

        # # 查询区间正在运行的时间点 [L,R]   o,l,r=1,1,u
        def query(o: int, l: int, r: int, L: int, R: int):
            if L <= l and r <= R: return cnt[o]
            m = (l + r) // 2
            pushdown(o, l, m, r)
            if m >= R: return query(o * 2, l, m, L, R)
            if m < L: return query(o * 2 + 1, m + 1, r, L, R)
            return query(o * 2, l, m, L, R) + query(o * 2 + 1, m + 1, r, L, R)

        # 在区间 [L,R] 的后缀上新增 suffix 个时间点    o,l,r=1,1,u
        # 相当于把线段树二分和线段树更新合并成了一个函数，时间复杂度为 O(log u)
        def update(o: int, l: int, r: int, L: int, R: int):
            size = r - l + 1
            if size == cnt[o]:
                return  # 全部都在运行中
            nonlocal suffix
            if L <= l and r <= R and size - cnt[o] <= suffix:  # 整个区间全部改为运行中
                suffix -= size - cnt[o]
                do(o, l, r)
                return
            m = (l + r) // 2
            pushdown(o, l, m, r)
            if m < R:
                update(o * 2 + 1, m + 1, r, L, R)  # 先更新右子树
            if suffix:
                update(o * 2, l, m, L, R)  # 在更新左子树（如果还有需要更新的时间点）
            cnt[o] = cnt[o * 2] + cnt[o * 2 + 1]

        for start, end, d in tasks:
            suffix = d - query(1, 1, u, start, end)  # 去掉运行中的时间点
            if suffix > 0: update(1, 1, u, start, end)  # 新增时间点
        return cnt[1]


