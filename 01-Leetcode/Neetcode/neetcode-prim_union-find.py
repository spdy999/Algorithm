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
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda e: e[2])
        uf = UninFind(n)
        minWt = 0
        cnt = 0
        for n1, n2, wt in edges:
            if uf.union(n1, n2):
                minWt += wt
                cnt += 1
        return minWt if cnt == n - 1 else -1

s = Solution()
assert s.minimumSpanningTree(5, [[0, 1, 10], [0, 2, 3], [1, 3, 2], [
                             2, 1, 4], [2, 3, 8], [2, 4, 2], [3, 4, 5]]) == 11
assert s.minimumSpanningTree(4, [[0, 1, 4], [1, 2, 7]]) == -1
assert s.minimumSpanningTree(5, [[0, 1, 2], [1, 2, 3], [3, 4, 5], [4, 3, 5]]) == -1
