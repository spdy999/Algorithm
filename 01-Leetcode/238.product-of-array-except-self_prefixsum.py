#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        prod = 1
        cntZr = 0

        for x in nums: # O(n)
            if x == 0:
                cntZr += 1
            if cntZr > 1:
                break
            if x != 0:
                prod *= x
        

        if cntZr >= 2:
            return ans

        if cntZr == 0:
            for i, x in enumerate(nums): # O(n)
                ans[i] = int(prod / x)
        else:
            ind = nums.index(0)
            ans[ind] = prod
        return ans
        
        # bigO = O(n)
# @lc code=end

