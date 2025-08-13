#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        n = len(coins)
        dp = dict()
        def dfs(i: int, summ: int, cnt: float) -> float:
            print('i:', i, 'summ:', summ, 'cnt:', cnt)
            if summ in dp:
                return dp[summ]
            if summ == 0:
                return cnt

            if summ < 0:
                return float('inf')
            minimum = min([dfs(i, summ - coins[i], cnt + 1) for i in range(n)])
            dp[summ] = minimum
            return minimum
        
        minn = min([dfs(i, amount, 0) for i in range(n)])
        return minn if minn != float('inf') else -1
  
s = Solution()
assert s.coinChange([1,2,5], 100) == 20
print(s.coinChange([186,419,83,408], 6249))
assert s.coinChange([186,419,83,408], 6249) == 20
        
# @lc code=end

