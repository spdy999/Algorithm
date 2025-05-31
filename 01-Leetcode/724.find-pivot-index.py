#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        n = len(nums)

        leftSum = 0
        for i in range(n):
            rightSum = tot - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]

        return -1
        
# @lc code=end

