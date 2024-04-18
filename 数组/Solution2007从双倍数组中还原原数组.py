from collections import Counter, deque
from typing import List


class Solution:
    # 首先把 changed 排序，并且统计所有元素出现的频数。
    #
    # 然后我们从小到大依次遍历数组，如果对于一个元素，它的频数大于零，并且它的两倍数也还在数组中，我们则可以把它加入到答案中。
    #
    # 如果对于一个数找不到它两倍数，即两倍数的频数等于零，则说明无法找到原数组，返回空数组即可。
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        count = Counter(changed)
        res = []
        for a in changed:
            if count[a] == 0:
                continue
            count[a] -= 1
            if count[a * 2] == 0:
                return []
            count[a * 2] -= 1
            res.append(a)
        return res

    def findOriginalArray1(self, changed: List[int]) -> List[int]:
        cnt = Counter(changed)
        if cnt[0] % 2 != 0:
            return []
        res = [0 for _ in range(cnt[0] // 2)]
        for e in sorted(cnt.keys()):
            if e == 0:
                continue
            cnt[e * 2] -= cnt[e]
            if cnt[e * 2] < 0:
                return []
            else:
                res.extend(e for _ in range(cnt[e]))
        return res

    def findOriginalArray2(self, changed: List[int]) -> List[int]:
        changed.sort()
        ans = []
        cnt = Counter()
        for x in changed:
            if x not in cnt:  # x不是双倍后的元素
                cnt[x * 2] += 1
                ans.append(x)
            else:  # x是双倍后的元素
                cnt[x] -= 1  # 清除一个标记
                if cnt[x] == 0:
                    del cnt[x]
        # 只有所有双倍标记都被清除掉，才能说明changed是一个双倍数组
        return [] if cnt else ans

    # 在方法一中，我们是小到大遍历 x=changed 的，所以加到哈希表中的 2x（双倍标记）也是从小到大的，并且最先加到哈希表中的双倍标记，也会最先清除掉。
    # 这种「先进先出」的性质启发我们把哈希表替换成更轻量的队列，队首就是下一个等待被清除的双倍标记。

    def findOriginalArray3(self, changed: List[int]) -> List[int]:
        changed.sort()
        ans = []
        queue = deque()
        for x in changed:
            if queue:
                if queue[0] < x:  # 无法配对
                    return []
                if queue[0] == x:  # 配对成功
                    queue.popleft()  # 清除一个标记
                    continue
            ans.append(x)
            queue.append(x * 2)  # 添加双倍标记
        # 只有所有双倍标记都被清除掉，才能说明changed是一个双倍数组
        return [] if queue else ans


Solution().findOriginalArray(changed=[6, 3, 0, 1])
