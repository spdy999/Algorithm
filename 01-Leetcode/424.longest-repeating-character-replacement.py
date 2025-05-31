#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window
        def winLen(ir, il):
            return ir - il + 1

        il, ir = 0, 0
        n = len(s)
        count = defaultdict(int)
        count[s[il]] += 1
        longest = 1

        for ir in range(1, n):
            count[s[ir]] += 1

            while winLen(ir, il) - max(count.values()) > k:
                count[s[il]] -= 1
                il += 1

            longest = max(longest, winLen(ir, il))

        return longest


assert Solution().characterReplacement("ABAB", 2) == 4, 'Should be 4'
assert Solution().characterReplacement("AABABBA", 1) == 4, 'Should be 4'

# @lc code=end
