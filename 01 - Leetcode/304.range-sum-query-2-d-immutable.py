#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r = len(matrix)
        c = len(matrix[0])
        self.sumMat = [[0] * (c + 1) for _ in range(r + 1)]

        for i in range(r):  # O(r * c)
            prefixRow = 0
            for j in range(c):
                prefixRow += matrix[i][j]
                topCell = self.sumMat[i][j + 1]

                self.sumMat[i + 1][j + 1] = prefixRow + topCell
        # matrix
        # [3, 0, 1, 4, 2]
        # [5, 6, 3, 2, 1]
        # [1, 2, 0, 1, 5]
        # [4, 1, 0, 1, 7]
        # [1, 0, 3, 0, 5]

        # self.sumMat
        # [0,  0,  0,  0,  0,  0]
        # [0,  3,  3,  4,  8, 10]
        # [0,  8, 14, 18, 24, 27]
        # [0,  9, 17, 21, 28, 36]
        # [0, 13, 22, 26, 34, 49]
        # [0, 14, 23, 30, 38, 58]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # O(1)

        # for using self.sumMat
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        rowDi = row1 - 1
        colDi = col1 - 1

        rowT = rowDi
        colT = col2

        rowL = row2
        colL = colDi

        bigMat = self.sumMat[row2][col2]
        topMat = self.sumMat[rowT][colT]
        lMat = self.sumMat[rowL][colL]
        diMat = self.sumMat[rowDi][colDi]

        return bigMat - topMat - lMat + diMat

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end
