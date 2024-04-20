from typing import List


class Solution:
    # 用dfs(i,left)来回溯，设当前枚举到candidates[i]，剩余要选的元素之和为left，按照选和不选进行分类
    # 不选 dfs(i+1,left)
    # 选 递归到dfs(i,left - candidates[i]).注意i不变，表示下次递归中还可以继续选candidates[i]
    # 如果递归中发现left为0，则说明找到了一个合法组合
    # 递归边界：如果i=n或者left <0
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int, left: int):
            if left == 0:
                # 找到一个合法组合
                ans.append(path.copy())
                return
            if i == len(candidates) or left < 0:
                return

            # 不选
            dfs(i + 1, left)
            # 选
            path.append(candidates[i])
            dfs(i, left - candidates[i])
            path.pop()  # 恢复现场

        dfs(0, target)
        return ans

    # 剪枝优化
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(i: int, left: int):
            if left == 0:
                # 找到一个合法组合
                ans.append(path.copy())
                return
            if i == len(candidates) or left < candidates[i]:
                return
            # 不选
            dfs(i + 1, left)
            # 选
            path.append(candidates[i])
            dfs(i, left - candidates[i])
            path.pop()  # 恢复现场

        dfs(0, target)
        return ans

    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(i: int, left: int):
            if left == 0:
                # 找到一个合法组合
                ans.append(path.copy())
                return
            if left < candidates[i]:
                return

            # 枚举哪一个
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                dfs(j, left - candidates[j])  # j不变表示还能选取
                path.pop()  # 恢复现场

        dfs(0, target)
        return ans
