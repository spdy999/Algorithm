#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        lpd = ['']

        def checkLpd(il: int, ir: int, lenPd: int):
            while il >= 0 and ir < n and s[il] == s[ir]:
                lenPd = ir - il + 1
                if lenPd > len(lpd[0]):
                    lpd[0] = s[il:ir+1]
                
                il-=1
                ir+=1

        for i in range(n): # O(n)
            # odd length
            checkLpd(i, i, 1)

            # even length
            checkLpd(i, i+1, 2)

        return lpd[0]

# @lc code=end
