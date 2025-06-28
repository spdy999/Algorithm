#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        numsSet = set(nums[:k + 1])

        if n <= 1 or n == len(numsSet) or k == 0:
            return False

        if len(numsSet) < k + 1:
            return True

        il = 0

        for ir in range(k + 1, n):
            l = nums[il]
            r = nums[ir]
            numsSet.remove(l)
            if r in numsSet:
                return True
            numsSet.add(r)

            il += 1
        return False
        
# @lc code=end

