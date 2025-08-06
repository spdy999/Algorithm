#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from typing import List
import sys
from typing import List
from collections import Counter

sys.setrecursionlimit(3000)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = dict()
        def dfs(i: int, summ: int) -> float:
            if summ in dp:
                return dp[summ]
            if summ == amount:
                return 0
            if summ > amount:
                return float('inf')
            dp[summ] = 1 + min([dfs(i, summ + coins[i]) for i in range(n)])
            return dp[summ]
        
        minn = min([dfs(i, 0) for i in range(n)])
        return minn if minn != float('inf') else -1



s = Solution()
assert s.coinChange([1, 2, 5], 100) == 20
# print(s.coinChange([186, 419, 83, 408], 6249))
assert s.coinChange([186, 419, 83, 408], 6249) == 20
assert s.coinChange([3, 7, 405, 436], 8839) == 25

# @lc code=end
