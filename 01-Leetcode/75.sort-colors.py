#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Bucket sort
        bucket = Counter(nums) # O(n)
        maxx = max(nums) + 1 # O(n)
        j = 0
        for i in range(maxx): # O(n)
            if i in bucket:
                for _ in range(bucket[i]):
                    nums[j] = i
                    j += 1
        return nums


assert Solution().sortColors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]
assert Solution().sortColors([2, 0, 1]) == [0, 1, 2]

# @lc code=end
