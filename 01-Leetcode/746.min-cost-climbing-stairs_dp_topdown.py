#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)

        n = len(cost)
        def rec(i):
            if i == -1 or i == -2:
                return
            
            rec(i + 1)
            a = cost[i + 1]
            b = cost[i + 2]
            cost[i] = min(cost[i] + a, cost[i] + b)
            
        rec(-n)
        return min(cost[:2])
        
# @lc code=end

