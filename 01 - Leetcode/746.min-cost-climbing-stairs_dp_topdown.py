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
        for i in range(-3, -n-1, -1):
            a = cost[i + 1]
            b = cost[i + 2]
            cost[i] = min(cost[i] + a, cost[i] + b)
        
        return min(cost[0:2])

        
# @lc code=end

