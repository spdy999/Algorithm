#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
import collections
import heapq
from typing import List


class UninFind:
    def __init__(self, n):
        self.par = dict()
        # technically is not effect the result but it helps find(n) faster (since tree is flat)
        self.rank = dict()

        for i in range(0, n):
            self.par[i] = i
            self.rank[i] = 1

    def find(self, x: int) -> int:
        if x == self.par[x]:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x1: int, x2: int) -> bool:
        p1, p2 = self.find(x1), self.find(x2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = self.par[p1]
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = self.par[p2]
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        # 1. create sorted edges
        eds = []
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                wt = abs(x1 - x2) + abs(y1 - y2)
                eds.append([i, j, wt])

        eds.sort(key=lambda e: e[2])
        uf = UninFind(n)
        minWt = 0
        for n1, n2, wt in eds:
            if uf.union(n1, n2):
                minWt += wt
        return minWt

s = Solution()
assert s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20
assert s.minCostConnectPoints([[3,12],[-2,5],[-4,1]]) == 18
        
# @lc code=end

