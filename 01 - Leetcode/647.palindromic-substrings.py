#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    cnt = 0
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        def checkPd(il, ir):
            while il >= 0 and ir < n and s[il] == s[ir]:
                self.cnt += 1
                il -= 1
                ir += 1
        
        for i in range(n):
            # odd len
            checkPd(i, i)

            # even len
            checkPd(i, i + 1)
        return self.cnt
        
# @lc code=end
