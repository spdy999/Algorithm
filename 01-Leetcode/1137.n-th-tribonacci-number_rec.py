#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        # rec, memo, top-down: trib(3) -> trib(2) -> trib(1) -> trib(0)
        memo = {0: 0, 1: 1, 2: 1}

        def rec(i):
            if i in memo:
                return memo[i]

            memo[i] = rec(i - 1) + rec(i - 2) + rec(i - 3)
            return memo[i]

        return rec(n)

# @lc code=end
