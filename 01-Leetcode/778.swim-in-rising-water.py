#
# @lc app=leetcode id=778 lang=python3
#
# [778] Swim in Rising Water
#

# @lc code=start
from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visit = set()  # {(x, y)}
        minHeap = [(grid[0][0], (0, 0))]  # [time, (x, y)]
        drs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # top, down, l, r
        r = len(grid) - 1
        l = len(grid[0]) - 1
        lastCo = (r, l)

        while minHeap:
            time, coor = heapq.heappop(minHeap)

            if coor == lastCo:
                return time

            x, y = coor
            for drx, dry in drs:
                neiX = x + drx
                neiY = y + dry
                neiCoor = (neiX, neiY)
                if neiCoor in visit or \
                        neiX < 0 or neiX > r or \
                        neiY < 0 or neiY > l:
                    continue

                maxT = max(time, grid[neiX][neiY])
                heapq.heappush(minHeap, ((maxT, neiCoor)))
                visit.add(neiCoor)


s = Solution()
assert s.swimInWater([[0, 2], [1, 3]]) == 3
assert s.swimInWater([[0, 1, 2, 3, 4],
                      [24, 23, 22, 21, 5],
                      [12, 13, 14, 15, 16],
                      [11, 17, 18, 19, 20],
                      [10, 9, 8, 7, 6], ]) == 16

# @lc code=end
