#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
import heapq
from typing import List
import collections


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t, w1)

            for n2, w2 in edges[n1]:
                if n2 not in visit:  # Greedy
                    heapq.heappush(minHeap, (w1 + w2, n2))

        return t if len(visit) == n else -1


assert Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
assert Solution().networkDelayTime([[1, 2, 1]], 2, 1) == 1
assert Solution().networkDelayTime([[1, 2, 1]], 2, 2) == -1

# @lc code=end
