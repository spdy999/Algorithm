#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]

        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum

        # Time = O(n)
        # Space = O(1)
        
# @lc code=end

