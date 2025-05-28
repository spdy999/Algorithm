#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [] # (dist, (x, y))
        ans = []
        for x, y in points: # O(n)
            dists.append((x**2 + y**2, (x, y)))
        heapq.heapify(dists) # O(log n)

        for i in range(k): # O(k)
            ans.append(heapq.heappop(dists)[1]) # O(log n)
        return ans
        # Time = O(k log n)
        # Space = O(n)

        
# @lc code=end
