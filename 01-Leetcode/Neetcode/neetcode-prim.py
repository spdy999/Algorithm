from typing import List
import collections
import heapq


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        visit = set() # prevent cycling (Acyclical)
        eds = collections.defaultdict(set)  # { u: (v, w) }
        minWt = 0

        for u, v, w in edges:
            eds[u].add((v, w))
            eds[v].add((u, w))

        minHeap = []  # (w, n1, n2)
        start = edges[0][0]  # [0,1,10]
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

        return minWt if len(visit) == n else -1


s = Solution()
assert s.minimumSpanningTree(5, [[0, 1, 10], [0, 2, 3], [1, 3, 2], [
                             2, 1, 4], [2, 3, 8], [2, 4, 2], [3, 4, 5]]) == 11
assert s.minimumSpanningTree(4, [[0, 1, 4], [1, 2, 7]]) == -1
assert s.minimumSpanningTree(5, [[0, 1, 2], [1, 2, 3], [3, 4, 5], [4, 3, 5]]) == -1
