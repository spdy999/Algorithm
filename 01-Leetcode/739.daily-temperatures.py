#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = [] # (index, t)
        
        for i, t in enumerate(temperatures): # O(n)
            while stack and t > stack[-1][1]:
                stI, stT = stack.pop()
                ans[stI] = i - stI
            stack.append((i, t))
        return ans
        
# @lc code=end

