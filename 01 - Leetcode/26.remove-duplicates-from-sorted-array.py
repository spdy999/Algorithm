#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        # remove from behind will prevent the index out of range while the list is resizing
        for i in range(n - 1, 0, -1):
            if nums[i - 1] == nums[i]:
                del nums[i-1] # .pop(i) can be used but I don't want to interact with the removed item
        return len(nums)
        
# @lc code=end

