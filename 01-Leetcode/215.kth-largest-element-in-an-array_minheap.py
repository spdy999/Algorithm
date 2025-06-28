#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: (n - k)O(log n)
        # Space: O(1)
        
        heapq.heapify(nums) # O(log n)

        while len(nums) > k: # O(n - k)
            heapq.heappop(nums) # O(log n)

        return nums[0]
        
        
# @lc code=end

