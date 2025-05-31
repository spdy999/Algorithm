#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] < nums[-1]:  # sorted
            return nums[0]
        if nums[-2] > nums[-1]:  # sorted desc
            return nums[-1]

        il = 0
        ir = n - 1

        bl = nums[0]

        while il <= ir:
            im = (il + ir) // 2
            m = nums[im]

            # print('l:', l, 'm:', m, 'r:', r)

            # m is the minimum. (no out of bound, it's filtered)
            if nums[im - 1] > m < nums[im + 1]:
                return m

            # adding = is a bit diff from general BST. This using bl(boundary left) not an exactly target. So there's only one chance for bl == m is it's against the left most. And the answer is on the 2nd index. Then I need to move the il to the right.
            if bl <= m:
                il = im + 1
            else:
                ir = im - 1

# @lc code=end
