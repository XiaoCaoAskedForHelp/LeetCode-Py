from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    res += 1
                    board[i][j] = '.'
                    idxi, idxj = i, j
                    while idxi + 1 < len(board) and board[idxi + 1][j] == 'X':
                        board[idxi + 1][j] = '.'
                        idxi += 1
                    while idxj + 1 < len(board[0]) and board[i][idxj + 1] == 'X':
                        board[i][idxj + 1] = '.'
                        idxj += 1
        return res

    def countBattleships1(self, board: List[List[str]]) -> int:
        # 对战舰的首个格子进行计数，当且仅当x格子的上方和左方不为x的时候为战舰首个格子
        m = len(board)
        n = len(board[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if i > 0 and board[i - 1][j] == 'X':
                    continue
                if j > 0 and board[i][j - 1] == 'X':
                    continue
                if board[i][j] == 'X':
                    ans += 1
        return ans


Solution().countBattleships([["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]])
