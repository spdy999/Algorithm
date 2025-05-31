#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)

        n = len(heights)
        maxArea = 0
        # monotonic stack increasing
        stack = [] # [(i, height)]

        for i, h in enumerate(heights): # O(n)
            start = i
            while stack and stack[-1][1] > h:
                prevI, prevH = stack.pop()
                start = prevI # will get the start of stack

                w = i - prevI
                area = prevH * w
                maxArea = max(maxArea, area)

            stack.append((start, h))
        
        for i, h in stack: # O(n)
            w = n - i
            area = h * w
            maxArea = max(maxArea, area)

        return maxArea

        
# @lc code=end

