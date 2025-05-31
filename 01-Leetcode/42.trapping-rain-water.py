#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        il = 0
        ir = len(height) - 1
        maxHl = height[il]
        maxHr = height[ir]
        summ = 0

        while il < ir:
            if maxHl < maxHr:
                il += 1
                hl = height[il]
                maxHl = max(maxHl, hl)
                summ += maxHl - hl
            else:
                ir -= 1
                hr = height[ir]
                maxHr = max(maxHr, hr)
                summ += maxHr - hr
        return summ


assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6, "Should be 6"
assert Solution().trap([4, 2, 0, 3, 2, 5]) == 9, "Should be 9"

# @lc code=end
