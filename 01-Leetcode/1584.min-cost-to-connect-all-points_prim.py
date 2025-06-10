#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
import collections
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        # 1. use n^2 loop to create edges (same as Combination)
        eds = collections.defaultdict(set)  # { u: (v, w) }
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                wt = abs(x1 - x2) + abs(y1 - y2)
                eds[i].add((j, wt))
                eds[j].add((i, wt))

        # 2. use Prim to find MST
        visit = set()
        minWt = 0
        minHeap = []  # (w, n1, n2)

        start = 0
        for v, w in eds[start]:
            minHeap.append((w, start, v))
        heapq.heapify(minHeap)
        visit.add(start)

        while minHeap:
            w, n1, n2 = heapq.heappop(minHeap)

            if n2 in visit:
                continue

            visit.add(n2)

            minWt += w

            for n3, w3 in eds[n2]:
                if n3 not in visit:
                    heapq.heappush(minHeap, (w3, n2, n3))

        return minWt

s = Solution()
assert s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20
assert s.minCostConnectPoints([[3,12],[-2,5],[-4,1]]) == 18
        
# @lc code=end

