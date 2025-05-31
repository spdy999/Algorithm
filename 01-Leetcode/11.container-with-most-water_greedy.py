#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Greedy, 2 pointers
        # bigO = O(n)

        # area = x * y
        # x = winLen(il, ir)
        # y = min(height[il], height[ir])

        def winLen(il, ir):
            return ir - il

        n = len(height)
        maxx = 0
        il = 0
        ir = n - 1

        while il < ir:
            x = winLen(il, ir)
            hl = height[il]
            hr = height[ir]
            y = min(hl, hr)
            area = x * y
            maxx = max(maxx, area)

            if hl < hr:
                il += 1
            else:
                ir -= 1

        return maxx


# @lc code=end
