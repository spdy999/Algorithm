#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return max(nums)
        
        nums.append(0)
        
        for i in range(n - 2, -1, -1):
            nums[i] = max(nums[i + 1], nums[i] + nums[i + 2])

        return max(nums[:2])


# @lc code=end

