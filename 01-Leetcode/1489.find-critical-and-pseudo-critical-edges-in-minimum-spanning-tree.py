#
# @lc app=leetcode id=1489 lang=python3
#
# [1489] Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
#

# @lc code=start
class UninFind:
    n = len(edges)
    par = dict()

    # technically is not effect the result but it helps find(n) faster (since tree is flat)
    rank = dict()

    for i in range(1, n + 1):
        par[i] = i
        rank[i] = 1

    def find(x: int) -> int:
        if x == par[x]:
            return x
        par[x] = find(par[x])
        return par[x]

    def union(x1: int, x2: int) -> bool:
        p1, p2 = find(x1), find(x2)

        if p1 == p2:
            return False

        if rank[p1] > rank[p2]:
            par[p2] = par[p1]
            rank[p1] += rank[p2]
        else:
            par[p1] = par[p2]
            rank[p2] += rank[p1]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        
# @lc code=end

