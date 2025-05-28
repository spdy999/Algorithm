#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i): # O(2^n)
            if i >= len(nums):
                return res.append(subset.copy())
            
            subset.append(nums[i])
            
            dfs(i + 1) # left

            subset.remove(nums[i])

            dfs(i + 1) # right

        dfs(0)

        return res

# @lc code=end

