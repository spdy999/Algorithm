#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 ->  000 dp[0] = 0
        # 1 ->  001 dp[1] = 1 + dp[1 - 1] 1 + dp[1 - 1] = 1
        # 2 ->  010 dp[2] = 1 + dp[2 - 1*2] = 1
        # 3 ->  011 dp[3] = 1 + dp[3 - 2] = 1 + 1 = 2
        # 4 ->  100 dp[n] = 1 + dp[n - 2*2] = 1 + 0 = 1
        # 5 ->  101 dp[5] = 1 + dp[5 - 4] = 1 + 1 = 2
        # 6 ->  110 dp[6] = 1 + dp[6 - 4] = 1 + 1 = 2
        #
        # 8 -> 1000 dp[8] = 1 + dp[n - 4*2]

        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n+1):
            if i == 2 * offset: # 4 == 2 * 2
                offset = i
            dp[i] = 1 + dp[i - offset]

        return dp


        
# @lc code=end

