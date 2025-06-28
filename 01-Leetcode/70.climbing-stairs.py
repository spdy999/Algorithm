#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # rec + fib + memo
        memo = {0: 1, 1: 1}

        def rec(i):
            if i in memo:
                return memo[i]
            
            memo[i] = rec(i - 1) + rec(i - 2)
            return memo[i]

        return rec(n)

        
# @lc code=end

