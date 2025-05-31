#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtrack(openP, closeP):
            if openP == closeP == n: # return when openP == closeP == n
                res.append("".join(stack))
                return
            
            if openP < n: # only add "(" if openP < n
                stack.append('(')
                backtrack(openP + 1, closeP)
                stack.pop()
            if closeP < openP: # only add ")" if closeP < openP
                stack.append(')')
                backtrack(openP, closeP + 1)
                stack.pop()

        backtrack(0, 0)
        return res
        
# @lc code=end

