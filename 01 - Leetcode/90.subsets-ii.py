#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(n log n)
        res = set()
        subset = []
        def dfs(i):
            if i >= len(nums):
                return res.add(tuple(subset.copy()))
            
            subset.append(nums[i])
            dfs(i + 1)
            
            subset.remove(nums[i])
            dfs(i + 1)
        
        dfs(0)
        return list(res)
        
# @lc code=end

