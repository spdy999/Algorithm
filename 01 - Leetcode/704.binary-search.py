#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        il = 0
        ir = n - 1
        
        while il <= ir:
            l = nums[il]
            r = nums[ir]
            im = (il + ir) // 2

            m = nums[im]
            if m == target:
                return im

            if target < m:
                ir = im - 1
            else:
                il = im + 1

        return -1

        
# @lc code=end

