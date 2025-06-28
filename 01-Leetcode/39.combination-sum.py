#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        comb = []
        res = []
        n = len(candidates)
        def dfs(i, summ):
            if summ == target:
                res.append(comb.copy())
                return
            if i >= n or summ > target:
                return
            
            cur = candidates[i]
            comb.append(cur)
            summ += cur
            dfs(i, summ) # Ref. subset

            summ -= comb.pop() # remove last
            dfs(i + 1, summ) # Ref. subset

        dfs(0, 0)
        return res
        
# @lc code=end

