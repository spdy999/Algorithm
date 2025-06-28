#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = [0]

        def checkPd(il, ir):
            while il >= 0 and ir < n and s[il] == s[ir]:
                cnt[0] += 1
                il -= 1
                ir += 1

        for i in range(n):
            # odd len
            checkPd(i, i)

            # even len
            checkPd(i, i + 1)
        return cnt[0]


s = Solution()
assert s.countSubstrings("aaa") == 6
assert s.countSubstrings("abc") == 3

# @lc code=end
