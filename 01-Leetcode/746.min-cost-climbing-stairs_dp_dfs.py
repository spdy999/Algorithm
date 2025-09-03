#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)

        n = len(cost)
        dp = dict() # i: summ
        def dfs(i: int) -> int:
            if i == n - 2 or i == n - 1:
                return cost[i]
            if i in dp:
                return dp[i]
            dp[i] = min(cost[i] + dfs(i + 1), cost[i] + dfs(i + 2))
            return dp[i]
        
        return min(dfs(0), dfs(1))

        
# @lc code=end

