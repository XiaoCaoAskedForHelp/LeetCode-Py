import bisect
from collections import defaultdict


class SnapshotArray:
    # 调用 set(index,val) 时，不去修改数组，而是往 index 的历史修改记录末尾添加一条数据：此时的快照编号和 val。
    def __init__(self, length: int):
        self.cur_snap_id = 0
        self.history = defaultdict(list)  # 每个index的历史修改记录

    def set(self, index: int, val: int) -> None:
        self.history[index].append((self.cur_snap_id, val))

    def snap(self) -> int:
        self.cur_snap_id += 1
        return self.cur_snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # 找快照编号 <= snap_id 的最后一次修改记录
        # 等价于找快照编号 >= snap_id+1 的第一个修改记录，它的上一个就是答案
        j = bisect.bisect_left(self.history[index], (snap_id + 1,)) - 1
        return self.history[index][j][1] if j >= 0 else 0


snapshotArr = SnapshotArray(2)  # 初始化一个长度为 3 的快照数组
snapshotArr.snap()
snapshotArr.get(1, 0)
snapshotArr.get(0, 0)
snapshotArr.set(1, 8)
snapshotArr.get(1, 0)
snapshotArr.snap()
snapshotArr.snap()
