#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        n = len(self.nums)
        self.preFix = [0] * n
        self.postFix = self.preFix.copy()

        self.preFix[0] = nums[0]
        self.postFix[-1] = nums[-1]
        self.summ = sum(self.nums)

        for i in range(1, n):
            self.preFix[i] = self.preFix[i - 1] + self.nums[i]
        # print(self.preFix)
        
        for i in range(-2, -n - 1, -1):
            self.postFix[i] = self.postFix[i + 1] + self.nums[i]
        # print(self.postFix)

    def sumRange(self, left: int, right: int) -> int:
        n = len(self.nums)
        pre = 0
        post = 0
        if left <= 0:
            left = 0
            pre = 0
        else:
            left -= 1
            pre = self.preFix[left]
        if right >= n - 1:
            right = n - 1
            post = 0
        else:
            right += 1
            post = self.postFix[right]

        return self.summ - pre - post
        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

