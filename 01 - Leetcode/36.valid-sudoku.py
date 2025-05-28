#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Time: O(n^2)
        # Space: O(2 * n^2)
        
        # check row, check col, check square
        rows = defaultdict(set) # r: {int, int, ... }
        cols = defaultdict(set) # c: {int, int, ... }
        sqs = defaultdict(set) # (r//3, c//3): {int, int, ... }

        for r in range(9):
            for c in range(9):
                x = board[r][c]
                if x == '.':
                    continue
                sq = (r//3, c//3)
                if (x in rows[r] or
                    x in cols[c] or
                    x in sqs[sq]):
                    return False
                
                rows[r].add(x)
                cols[c].add(x)
                sqs[sq].add(x)
        # print('rows:', rows)
        # print('cols:', cols)
        # print('sqs:', sqs)

        return True
        
# @lc code=end

