#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Bucket sort
        bucket = Counter(nums)
        maxx = max(nums) + 1
        j = 0
        for i in range(maxx):
            if i in bucket:
                for _ in range(bucket[i]):
                    nums[j] = i
                    j += 1

        
# @lc code=end

