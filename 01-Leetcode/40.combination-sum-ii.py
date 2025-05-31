#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # O (n log n)
        comb = []
        res = []
        n = len(candidates)

            
        def backtrack(pos, target):
            if target == 0: # base case
                res.append(comb.copy())
            if target <= 0: # base case
                return

            prev = -1
            for i in range(pos, n):
                candidate = candidates[i]
                if candidate == prev:
                    continue
                comb.append(candidates[i])
                backtrack(i + 1, target - candidate)
                comb.pop()
                prev = candidate
        backtrack(0, target)

        return res
        
# @lc code=end

