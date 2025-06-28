#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # bigO = O(n^2)

        nums.sort()  # O(n log n) => [ -4, -1, -1, 0, 1, 2 ]
        n = len(nums)
        res = []
        for i, num in enumerate(nums[:-1]):  # O(n)
            target = 0 - num
            # skip duplicate for [ -4, -1, -1, 0, 1, 2 ] : eg. skip next -1
            if i > 0 and num == nums[i - 1]:
                continue
            ir = n - 1
            il = i + 1

            while il < ir:  # O(n) from this point is [[167. Two Sum II - Input Array Is Sorted]]
                # skip duplicate for [-2,0,0,2,2] : next 0
                if il > i + 1 and nums[il] == nums[il - 1]:
                    il += 1
                    continue
                summ = nums[il] + nums[ir]
                if summ == target:
                    res.append((num, nums[il], nums[ir]))  # O(1)
                    il += 1
                    continue
                elif summ < target:
                    il += 1
                    continue
                elif summ > target:
                    ir -= 1
                    continue
        return res

# @lc code=end
