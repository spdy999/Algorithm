import collections
from typing import Dict, List
import heapq


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        ed = collections.defaultdict(list)
        t = dict()  # { node: shortest distance }
        for i in range(n):
            t[i] = -1

        for u, v, w in edges:
            ed[u].append((v, w))
        minHeap = [(0, src)]
        visit = set()

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            visit.add(n1)
            t[n1] = max(t[n1], w1)

            for n2, w2 in ed[n1]:
                if n2 not in visit:
                    heapq.heappush(
                        minHeap, (w1 + w2, n2))

        return t


def test():
    solution = Solution()
    assert solution.shortestPath(
        3, [[0, 1, 4]], 0) == dict({0: 0, 1: 4, 2: -1})
    assert solution.shortestPath(
        5,
        [[0, 1, 10], [0, 2, 3], [1, 3, 2], [2, 1, 4],
            [2, 3, 8], [2, 4, 2], [3, 4, 5]],
        0,
    ) == dict({0: 0, 1: 7, 2: 3, 3: 9, 4: 5})


if __name__ == "__main__":
    test()
    print("Correct Dijkstra's shortest path")
