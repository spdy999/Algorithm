#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        il = 0
        ml = 0
        n = len(s)
        checkChars = set()
        
        for ir in range(n):
            while s[ir] in checkChars: # 1.check duplicated
                checkChars.remove(s[il]) # 2. remove l pointer char
                il += 1 # 3. increase l pointer

            checkChars.add(s[ir]) # 4. continue adding char
            ml = max(ml, ir - il + 1) # compare current winLen to old ml

        return ml

        # bigO = O(n)
        # two-pointers
        
# @lc code=end

