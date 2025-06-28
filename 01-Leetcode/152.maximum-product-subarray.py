#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
            tmpCurMax = curMax * n
            tmpCurMin = curMin * n
            curMax = max(tmpCurMax, tmpCurMin, n)
            curMin = min(tmpCurMax, tmpCurMin, n)
            res = max(res, curMax)
        return res


# @lc code=end
