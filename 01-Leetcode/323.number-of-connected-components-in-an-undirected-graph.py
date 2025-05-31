class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = dict()
        rank = dict()

        for i in range(n):
            par[i] = i
            rank[i] = 1

        def find(x: int) -> int:
            if x == par[x]:
                return x
            par[x] = find(par[x])

            return par[x]

        def union(x1: int, x2: int) -> int:
            p1, p2 = find(x1), find(x2)

            if p1 == p2:
                return 0

            if rank[p1] > rank[p2]:
                par[p2] = par[p1]
                rank[p1] += rank[p2]
            else:
                par[p1] = par[p2]
                rank[p2] += rank[p1]
            return 1

        res = n
        for x1, x2 in edges:
            res -= union(x1, x2)

        return res
