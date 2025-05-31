#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
        
    def helper(self, nums):
        n = len(nums)
        nums[1] = max(nums[:2])

        for i in range(2, n):
            nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])
            
        return max(nums[-2:])
 
# @lc code=end

