#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        preFix = [0] * n

        total = 0
        for i in range(n):  # O(n)
            total += nums[i]
            preFix[i] = total

        # print(preFix)
        for i in range(n):  # O(n)
            if i == 0:
                if total - preFix[0] == 0:
                    return 0
            elif i == n - 1:
                if total - nums[n - 1] == 0:
                    return n - 1
            else:
                if preFix[i - 1] == total - preFix[i]:
                    return i

        return -1
        
# @lc code=end

