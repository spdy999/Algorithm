#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Time : O(n log k)
        # Space : O(k)
        hq = []
        for x, y in points: # O(n)
            s = -(x**2 + y**2)
            if len(hq) < k:
                heapq.heappush(hq, [s, (x, y)]) # O(log k)
            elif len(hq) > k:
                heapq.heappop(hq) # O(log k)
            elif hq and s > hq[0][0]:
                heapq.heappop(hq) # O(log k)
                heapq.heappush(hq, [s, (x, y)]) # O(log k)
        return [[x, y] for s, [x,y] in hq] # O(k)

        
# @lc code=end

