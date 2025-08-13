#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Combination sum
        coins = sorted(coins) # TODO: necessary?
        comb = []
        n = len(coins)
        dp = dict() # { summ: amount }
        cnt = [0]
        def dfs(i, summ):
            # if summ in dp:
            #     return dp[summ]
            if summ == amount:
                # res.append(comb.copy())
                cnt[0] += 1
                return
            if i >= n or summ > amount:
                return
            
            cur = coins[i]
            comb.append(cur)
            summ += cur
            dfs(i, summ) # Ref. subset

            summ -= comb.pop() # remove last
            dfs(i + 1, summ) # Ref. subset

        dfs(0, 0)
        # return len(res)
        return cnt[0]
s = Solution()
# print(s.change(500, [3,5,7,8,9,10,11]))
assert s.change(500, [3,5,7,8,9,10,11]) == 35502874
# @lc code=end

