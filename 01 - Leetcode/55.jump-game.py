#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        last_ind = n - 1
        goal = last_ind
        for i in range(last_ind, -1, -1):
            if i + nums[i] >= goal:
                goal = i
            
        return True if goal <= 0 else False
        # 1-pass
        # Time : O(n)
        # Space : O(1)
        
# @lc code=end

