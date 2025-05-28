#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxx = 0
        checkC = set()
        for i in range(n): # O(n)
            for j in range(i, n): # O(n)
                if s[j] in checkC:
                    checkC = set()
                    break
                maxx = max(maxx, j - i + 1)
                checkC.add(s[j])
        return maxx

        # bigO = O(n^2)
        # two-pointers
        
# @lc code=end

