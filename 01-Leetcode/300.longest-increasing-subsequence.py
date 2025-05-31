#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#


# @lc code=start
# Neetcode
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Time: O(n^2)
        # Space: O(n)

        # [1, 2, 4, 3]
        n = len(nums)
        LIS = [1] * n
        maxx = 1
        for i in range(n - 1, -1, -1): # O(n)
            for j in range(i, n): # O(n)
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                    maxx = max(LIS[i], maxx)
        return maxx


# @lc code=end
