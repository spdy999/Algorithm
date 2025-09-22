#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:

        hqSt = []
        hqL = []
        for i,p in enumerate(list(s)):
            if p == '(':
                heappush(hqL, -i)
            if p == '*':
                heappush(hqSt, -i)
            if p == ')':
                if hqL:
                    heappop(hqL) # confirm hqL is infront of current P
                elif hqSt:
                    heappop(hqSt) # confirm hqSt is infront of current P
                else:
                    return False # ")", ")*"
        while hqL and hqSt:
            if -hqL[0] < -hqSt[0]:
                heappop(hqL)
                heappop(hqSt)
            else:
                return False
        return False if hqL else True
        
# @lc code=end

