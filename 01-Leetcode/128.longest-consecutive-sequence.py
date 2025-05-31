#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)

        numSet = set(nums)  # O(n)
        maxx = 0

        for num in numSet:  # O(n)
            if num - 1 not in numSet:  # check if it a start of a set
                length = 0
                while num + length in numSet:
                    length += 1
                maxx = max(maxx, length)

        return maxx


# @lc code=end
