#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        # rec, memo, top-down: fib(3) -> fib(2) -> fib(1) -> fib(0)
        memo = {0: 0, 1: 1}

        def rec(i):
            if i in memo:
                return memo[i]
            
            memo[i] = rec(i - 1) + rec(i - 2)
            return memo[i]

        return rec(n)
        
# @lc code=end

