#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower() # substitute every character which is not alhanumeric to ''. Then, lower every left over charactor
        n = len(s)

        # Easiest palindrome checking, (no need to care about odd or even length)
        l = 0
        r = n - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

        
# @lc code=end

