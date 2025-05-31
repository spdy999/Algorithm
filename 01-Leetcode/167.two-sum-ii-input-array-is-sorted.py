#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointers : bigO = O(n)

        n = len(numbers)

        l = 0  # first index
        r = n - 1  # last index

        while l < r:  # O(n)
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l + 1, r + 1]

            if summ > target:  # too much, decrease value by moving right ind to left
                r -= 1
            else:  # too less, increase value by moving left ind to right
                l += 1


# @lc code=end
