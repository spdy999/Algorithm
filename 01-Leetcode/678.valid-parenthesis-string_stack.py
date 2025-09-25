#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        st = [] # star
        l = [] # left parenthesis
        for i,p in enumerate(list(s)):
            if p == '(':
                l.append(i)
            if p == '*':
                st.append(i)
            if p == ')':
                if l:
                    l.pop() # confirm l is infront of current P
                elif st:
                    st.pop() # confirm st is infront of current P
                else:
                    return False # ")", ")*"
        while l and st:
            if l[-1] < st[-1]:
                l.pop()
                st.pop()
            else:
                return False
        return False if l else True
        
# @lc code=end

