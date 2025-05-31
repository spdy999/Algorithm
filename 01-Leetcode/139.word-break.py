#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[-1] = True # base case
        
        for i in range(n - 1, -1, -1):
            for w in wordDict:
                len_w = len(w)
                word_end_ind = i + len_w
                # "dp[i] is False" needed to prevent some word might flip back what is already partitioned(True) eg. s="abcd" wordDict=["a","abc","b","cd"]
                if dp[i] is False and word_end_ind <= n and s[i: word_end_ind] == w:
                    dp[i] = dp[word_end_ind]
        return dp[0]
        
# @lc code=end

