#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#

# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        summ = sum(stones)
        dp = dict() # (i, tot): min(dp)
        half = summ // 2
        n = len(stones)
        def dfs(i: int, tot: int) -> int:
            if tot >= half or i == n:
                return abs(tot - (summ - tot))
            if (i, tot) in dp:
                return dp[(i, tot)]
            dp[(i, tot)] = min(dfs(i + 1, tot), dfs(i + 1, tot + stones[i]))
            return dp[(i, tot)]

        return dfs(0, 0)
# @lc code=end

