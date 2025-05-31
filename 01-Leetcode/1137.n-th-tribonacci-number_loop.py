#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        # loop, btm-up: trib(0) -> trib(1) -> trib(2) -> trib(3)
        
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1

        trib = [0] * (n + 1)
        trib[1] = 1
        trib[2] = 1

        for i in range(3, n + 1):
            trib[i] = trib[i - 1] + trib[i - 2] + trib[i - 3]
        
        return trib[n]

        
# @lc code=end

