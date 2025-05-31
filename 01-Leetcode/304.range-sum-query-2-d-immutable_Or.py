#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.oldMat = copy.deepcopy(matrix)
        self.r = len(matrix)
        self.c = len(matrix[0])
        tot = 0
        for i in range(self.r):  # O(r * c)
            for j in range(self.c):
                tot += matrix[i][j]
                matrix[i][j] = tot
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        colR = col2

        tot = 0
        for i in range(row1, row2 + 1):  # O(r)
            tot += self.matrix[i][colR] - (self.matrix[i][col1] - self.oldMat[i][col1])
        return tot

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

