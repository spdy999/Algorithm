#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        # there will be no route if the obstacle is at the end or start of the route
        if obstacleGrid[rows - 1][cols - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        cache = dict()
        cache[(rows - 1, cols - 1)] = 1


        def dfs_cache(r, c):
            if r >= rows or c >= cols:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            if obstacleGrid[r][c] == 1:
                return 0
                                      # down,                right
            cache[(r, c)] = dfs_cache(r + 1, c) + dfs_cache(r, c + 1)

            return cache[(r, c)]
        
        dfs_cache(0, 0)
        return cache[(0, 0)]
        
# @lc code=end

