#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        last_ind = n - 1
        mem = {}

        if n <= 2:
            return max(nums)
        
        def rec(i: int, summ: int) -> int:
            if i in mem:
                return summ + mem[i]
            if i > last_ind:
                return summ
            if i == last_ind or i == last_ind - 1:
                return summ + nums[i]                                   
            else:
                maxi = max(rec(i+2, summ + nums[i]), rec(i+3, summ + nums[i]))
                mem[i] = maxi - summ
                return maxi
            
        return max(rec(0, 0), rec(1, 0))

# @lc code=end

