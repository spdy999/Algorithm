#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # Stack : LIFO
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for c in s:
            if c in pairs: # append left side to stack
                stack.append(c)
            else: # check right side matching
                if len(stack) == 0: # if there's right side but left side already empty => no matching
                    return False
                left = stack.pop()
                if pairs[left] is c:
                    continue
                else:
                    return False

        return len(stack) == 0
        
# @lc code=end

