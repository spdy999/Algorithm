#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)  # O(n)

        while len(stones) > 1:
            y = -heapq.heappop(stones)  # O(log n)
            x = -heapq.heappop(stones)  # O(log n)

            diff = y - x

            if diff > 0:
                heapq.heappush(stones, -diff)  # O(log n)

        return 0 if len(stones) == 0 else -stones[0]

# @lc code=end
