#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        comb = []
        def bt(i: int):
            res.append(comb.copy())

            for j in range(i, n):
                comb.append(nums[j])
                bt(j + 1)
                comb.pop()

        bt(0)
        return res

# @lc code=end

