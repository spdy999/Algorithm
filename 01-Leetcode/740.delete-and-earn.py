#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        earn1, earn2 = 0, 0
        
        for i in range(len(nums)):
            curVal = nums[i] * count[nums[i]]

            # earn2 can't be used
            if i > 0 and nums[i] == nums[i - 1] + 1:
                tmp = earn2
                earn2 = max(earn2, earn1 + curVal)
                earn1 = tmp
            else: # earn2 is fine
                tmp = earn2
                earn2 += curVal
                earn1 = tmp
        
        return earn2
        
# @lc code=end

