#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute force => TLE
        # bigO = O(n^2)

        # area = x * y
        # x = winLen(il, ir)
        # y = min(height[il], height[ir])
        def winLen(il, ir):
            return ir - il
        
        n = len(height)
        maxx = 0

        for i in range(n):
            for j in range(i + 1, n):
                x = winLen(i, j)
                y = min(height[i], height[j])

                area = x * y
                maxx = max(maxx, area)
        return maxx


# @lc code=end

