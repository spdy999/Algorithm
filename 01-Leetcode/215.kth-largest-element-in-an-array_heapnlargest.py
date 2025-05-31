#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest = heapq.nlargest(k, nums)
        return largest[-1]       
        
# @lc code=end

