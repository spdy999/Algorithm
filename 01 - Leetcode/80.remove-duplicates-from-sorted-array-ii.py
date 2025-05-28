#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        cnt = 1
        n = len(nums)
        for r in range(1, n):  # O(n)
            if nums[r - 1] == nums[r]:
                cnt += 1
            if nums[r - 1] != nums[r]:
                nums[l] = nums[r]
                l += 1
                cnt = 1
                continue

            if cnt == 2:
                nums[l] = nums[r]
                l += 1

        return l
        
# @lc code=end

