#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        pl = prices[0]

        for i in range(1, n):
            pr = prices[i]
            profit = max(profit, pr - pl)
            
            if pr < pl:
                pl = pr
                
        return profit

# @lc code=end

