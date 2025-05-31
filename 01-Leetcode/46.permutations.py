#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack_dfs(head, tail):
            if len(tail) == n:
                res.append(tail)
                return
             
            for i in range(len(head)):
                new_head = head[:i] + head[i+1:]
                new_tail = tail + [head[i]]
                backtrack_dfs(new_head, new_tail)
            
        backtrack_dfs(nums, [])
        return res

        
# @lc code=end

