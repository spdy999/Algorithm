#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        minL = 0
        maxL = 0
        for p in s:
            if p == '(':
                minL += 1
                maxL += 1
            elif p == ')':
                minL -= 1
                maxL -= 1
            else:
                minL -= 1
                maxL += 1

            if minL < 0:
                minL = 0
            if maxL < 0:
                return False
        return minL == 0

# @lc code=end

