#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_t = len(t)
        len_s = len(s)
        if len_s == len_t and s == t:
            return True
        if len_s == 0:
            return True
        if len_t < len_s:
            return False

        def rec(i_s: int, i_t: int) -> bool:
            if i_t >= len_t or i_s >= len_s:
                return False
            if s[i_s] == t[i_t]:
                # print(s[i_s], t[i_t])
                if i_s == len_s - 1:
                    return True

                return rec(i_s + 1, i_t + 1)
            else:
                return rec(i_s, i_t+1)

        return rec(0, 0)
        
# @lc code=end

