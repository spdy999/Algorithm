#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] < nums[-1]:  # sorted asc  => nums = [1,2,3,4]
            return nums[0]
        if nums[-2] > nums[-1]: # sorted desc => nums = [4,3,2,1]
            return nums[-1]
        
        il = 0
        ir = n - 1
        
        bl = nums[0]

        # BST
        while il <= ir:
            im = (il + ir) // 2
            m = nums[im]
            l = nums[il]
            r = nums[ir]

            # print('l:', l, 'm:', m, 'r:', r)

            if nums[im - 1] > m < nums[im + 1]: # m is the minimum. (no out of bound, it's filtered)
                return m

            if bl <= m: # adding = is a bit diff from general BST. This using bl(boundary left) not an exactly target. So there's only one chance for bl == m is it's against the left most. And the answer is on the 2nd index. Then I need to move the il to the right.
                il = im + 1
            else:
                ir = im - 1
            
        return -1 # TODO: remove
        
# @lc code=end

