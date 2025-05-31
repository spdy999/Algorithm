#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.hp = nums.copy()
        heapq.heapify(self.hp) # O(n)

    def add(self, val: int) -> int:
        heapq.heappush(self.hp, val) # O(log n)
        while len(self.hp) > self.k:
            heapq.heappop(self.hp) # O(log n)
        return self.hp[0] # O(1)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

