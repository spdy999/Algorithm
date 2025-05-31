#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        n = len(nums)
        for r in range(1, n):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l


        
# @lc code=end

