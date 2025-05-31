#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)

        for i in range(n - 1):
            diff = prices[i + 1] - prices[i]
            if diff > 0:
                profit += diff
        return profit
# @lc code=end

