#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tstack = []
        zipp = sorted(zip(position, speed), reverse=True) # O(n log n)  # [[10, 2], [8, 4], [5, 1], [3, 3], [0, 1]]

        for p, v in zipp:
            s = target - p
            t = s / v
            if tstack:
                if tstack[-1] < t:
                    tstack.append(t)
            else:
                tstack.append(t)
        return len(tstack)
        # [[10, 2], [8, 4], [5, 1], [3, 3], [0, 1]]
        # stack: [1.0]
        # stack: [1.0, 1.0]
        # stack: [1.0, 7.0]
        # stack: [1.0, 7.0, 3.0]
        # stack: [1.0, 7.0, 12.0]

        
# @lc code=end

