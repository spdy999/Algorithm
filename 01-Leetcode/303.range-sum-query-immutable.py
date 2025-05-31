#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        summ = 0
        self.preFix = [0] * n  # space = O(n)

        for i in range(0, n):  # O(n)
            summ += nums[i]
            self.preFix[i] = summ


    def sumRange(self, left: int, right: int) -> int:
        preRight = self.preFix[right]
        preLeft = 0 if left <= 0 else self.preFix[left - 1]
        return preRight - preLeft

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

