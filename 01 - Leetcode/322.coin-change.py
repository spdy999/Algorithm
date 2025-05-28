#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        setc = set(coins) # O(n)

        for a in range(1, amount + 1): # O(amount)
            if a in setc: # this if is for my understanding (relate to excalidraw)
                dp[a] = 1
                continue
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[-1] if dp[-1] <= amount else -1
        
# @lc code=end

