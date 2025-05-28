#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])

        il = 0
        ir = rows * cols - 1

        while il <= ir:
            im = (il + ir) // 2
            imr, imc = [im // cols, im % cols]
            check = matrix[imr][imc]

            if check == target:
                return True
            
            if  target < check:
                ir = im - 1
            else:
                il = im + 1
        
        return False
        
# @lc code=end

