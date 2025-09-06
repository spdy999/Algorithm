#
# @lc app=leetcode id=2133 lang=python3
#
# [2133] Check if Every Row and Column Contains All Numbers
#

# @lc code=start
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        # check rows, check cols
        rows = len(matrix)
        cols = len(matrix[0])
        dRows = defaultdict(set)
        dCols = defaultdict(set)
        
        for r in range(rows):
            for c in range(cols):
                val = matrix[r][c] 
                if (val in dRows[r] or
                    val in dCols[c]):
                    return False
                dRows[r].add(val)
                dCols[c].add(val)
        
        return True

        
# @lc code=end

