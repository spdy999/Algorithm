#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        # loop, btm-up: fib(0) -> fib(1) -> fib(2) -> fib(3)

        if n < 2:
            return n

        fibo = [0] * (n + 1)
        fibo[1] = 1

        for i in range(2, n + 1):  # O(n)
            fibo[i] = fibo[i - 1] + fibo[i - 2]

        return fibo[n]


assert Solution().fib(0) == 0
assert Solution().fib(1) == 1
assert Solution().fib(2) == 1
assert Solution().fib(10) == 55

# @lc code=end
