#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for i in range(n)]
        posDiag = set()
        negDiag = set()
        col = set()

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                pos = r + c
                neg = r - c
                if c in col or pos in posDiag or neg in negDiag:
                    continue
                
                col.add(c)
                posDiag.add(pos)
                negDiag.add(neg)
                board[r][c] = 'Q'
                # print('col:', col)
                # print('posDiag:', posDiag)
                # print('negDiag:', negDiag)
                # print('----')
                backtrack(r + 1)
                
                col.remove(c)
                posDiag.remove(pos)
                negDiag.remove(neg)
                board[r][c] = '.'
 
        backtrack(0)
        return res
        
# @lc code=end

