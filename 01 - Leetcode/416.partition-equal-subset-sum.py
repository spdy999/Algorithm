#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Time: O(n^2)
        # Space: O(2n) -> O(n)
        summ = sum(nums)
        if summ % 2  is not 0: # odd + odd = even, even + even = even
            return False
        
        dp = set()
        dp.add(0)
        target = summ // 2
        n = len(nums)

        for i in range(n - 1, -1, -1): # O(n)
            nextDp = set()
            nextDp = dp.copy()
            for t in dp: # O(n)
                nextDp.add(t + nums[i])
            dp = nextDp

        return True if target in dp else False # can use early return before line 25
        
# @lc code=end

