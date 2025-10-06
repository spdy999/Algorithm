#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        found = float('inf')
        while l <= r:
            mid = (l + r) // 2
            isBad = isBadVersion(mid)
            if isBad: # found or on left
                r = mid - 1
                found = mid
                 
            else: # on right
                l = mid + 1
        return found
        
# @lc code=end

