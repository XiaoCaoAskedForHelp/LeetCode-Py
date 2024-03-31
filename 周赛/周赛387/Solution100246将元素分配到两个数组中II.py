from typing import List

from sortedcontainers import SortedList


class Solution:

    def search(self, list: SortedList, num: int, start: int, end: int):
        if start > end:
            return start
        mid = (start + end) // 2
        if num >= list[mid]:
            start = mid + 1
        else:
            end = mid - 1
        return self.search(list, num, start, end)

    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        sl1 = SortedList(arr1)
        sl2 = SortedList(arr2)
        for num in nums[2:]:
            # cnt1 = len(sl1) - sl1.bisect_right(num)
            # cnt2 = len(sl2) - sl2.bisect_right(num)
            cnt1 = len(sl1) - self.search(sl1, num, 0, len(sl1) - 1)
            cnt2 = len(sl2) - self.search(sl2, num, 0, len(sl2) - 1)
            if cnt1 > cnt2:
                arr1.append(num)
                sl1.add(num)
            elif cnt1 < cnt2:
                arr2.append(num)
                sl2.add(num)
            else:
                if len(arr1) <= len(arr2):
                    arr1.append(num)
                    sl1.add(num)
                else:
                    arr2.append(num)
                    sl2.add(num)
        return arr1 + arr2


Solution().resultArray([2, 1, 3, 3])
Solution().resultArray([5, 14, 3, 1, 2])
