#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board is None or len(board) == 0:
            return False
        
        rows = len(board)
        cols = len(board[0])
        n = len(word)
        path = set()
        drs = ((-1, 0), (1, 0), (0, -1), (0, 1)) # top, btm, lft, rgt

        def dfs(r, c, i):
            if i == n:
                return True
            
            # out of bound, not interest, already in path
            if (not (0 <= r < rows) or not (0 <= c < cols) or
                board[r][c] != word[i] or
                (r, c) in path):
                return False

            path.add((r, c))
            res = any([dfs(r + drr, c + drc, i + 1) for drr, drc in drs]) # traverse in 4 directions
            path.remove((r, c)) # backtracking
            
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False
    
# @lc code=end

