#
# @lc app=leetcode id=1489 lang=python3
#
# [1489] Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
#

# @lc code=start
class UninFind:
    def __init__(self, n):
        self.par = dict()
        # technically is not effect the result but it helps find(n) faster (since tree is flat)
        self.rank = dict()

        for i in range(n):
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
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        # 1. create sorted edges
        for i, e in enumerate(edges):
            e.append(i)

        edges.sort(key=lambda e: e[2])
        uf = UninFind(n)
        mst = 0

        # 2. Find MST
        for n1, n2, wt, i in edges:
            if uf.union(n1, n2):
                mst += wt

        critical, pseudo = [], []
        for n1, n2, nwt, i in edges:
            # Try without curr edge
            checkMst = 0
            uf1 = UninFind(n)
            for v1, v2, vwt, j in edges:
                if i != j and uf1.union(v1, v2):
                    checkMst += vwt
            if max(uf1.rank.values()) != n or checkMst > mst:
                critical.append(i)
                continue

            # Try with curr edge
            uf2 = UninFind(n)
            uf2.union(n1, n2)
            checkMst = nwt
            for v1, v2, vwt, j in edges:
                if uf2.union(v1, v2):
                    checkMst += vwt
            if mst == checkMst:
                pseudo.append(i)
        return [critical, pseudo]

# @lc code=end

