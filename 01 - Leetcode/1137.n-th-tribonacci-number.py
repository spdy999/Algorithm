#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#

# @lc code=start
class Solution:
    mem = {0: 0, 1:1, 2:1}
    def tribonacci(self, n: int) -> int:
        t = [0, 1, 1]
        if n in self.mem:
            return self.mem[n]

        summ = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        self.mem[n] = summ
        return summ
        
# @lc code=end

