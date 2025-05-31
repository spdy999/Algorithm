#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    # TC: O(n), 1 pass
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict() # { val: index }
        for i, n in enumerate(nums):  # O(n)
            diff = target - n
            if diff in hashmap:
                return [i, hashmap[diff]]
            hashmap[n] = i

        
# @lc code=end

