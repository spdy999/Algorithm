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


# class Solution:
#     def coinChange(self, coins: List[int], amount: int):
#         # coins.sort(reverse=True)
#         memo = {}
#
#         def dp(n, cnt):
#             # print('n:', n, 'cnt:', cnt)
#             if n == 0:
#                 return 0, []
#             if n < 0:
#                 return float('inf'), []
#             if n in memo:
#                 return memo[n]
#
#             min_coins = float('inf')
#             min_combo = []
#
#             for coin in coins:
#                 res, combo = dp(n - coin, cnt + 1)
#                 if res + 1 < min_coins:
#                     min_coins = res + 1
#                     min_combo = combo + [coin]
#
#             memo[n] = (min_coins, min_combo)
#             # print()
#             return memo[n]
#
#         min_coins, combo = dp(amount, 0)
#         if min_coins == float('inf'):
#             return -1
#         else:
#             # print(f"Minimum coins needed: {min_coins}")
#             # print(f"Combination: {Counter(combo)}")
#             # print(f"Check sum: {sum(combo)}")
#             return min_coins

# # Example usage:
# coins = [186, 419, 83, 408]
# amount = 6249

# sol = Solution()
# min_coins, combination = sol.coinChange(coins, amount)
# print(f"Minimum coins needed: {min_coins}")
# print(f"Combination: {combination}")
# print(f"Check sum: {sum(combination)}")


sys.setrecursionlimit(3000)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = dict()

        def dfs(i: int, summ: int, cnt: float) -> float:
            # print('i:', i, 'summ:', summ, 'cnt:', cnt)
            if (summ, cnt) in dp:
                # print('....1')
                return dp[(summ, cnt)]
            if summ == amount:
                # print('....2')
                return cnt
            if summ > amount:
                # print('....3')
                return float('inf')
            dp[(summ, cnt)] = min([dfs(i, summ + coins[i], cnt + 1) for i in range(n)])
            # print()
            # print()
            return dp[(summ, cnt)]

        minn = min([dfs(i, 0, 0) for i in range(n)])
        return minn if minn != float('inf') else -1


s = Solution()
assert s.coinChange([1, 2, 5], 100) == 20
# print(s.coinChange([186, 419, 83, 408], 6249))
assert s.coinChange([186, 419, 83, 408], 6249) == 20
assert s.coinChange([3, 7, 405, 436], 8839) == 25

# @lc code=end
