#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = dict() # (r,c): summ
        cache[(m-1, n-1)] = 1
        def dfs_cache(r, c):
            if r >= m or c >= n:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]

                          # down,                right
            cache[(r,c)] = dfs_cache(r + 1, c) + dfs_cache(r, c + 1)
            
            return cache[(r,c)]
        
        dfs_cache(0, 0)
        return cache[(0, 0)]
# @lc code=end

