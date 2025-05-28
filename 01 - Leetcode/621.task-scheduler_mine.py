#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks) # O(n)
        interval = 0
        maxHq = [-v for v in cnt.values()] # O(n)
        heapq.heapify(maxHq) # O(log n)

        while maxHq: # O(n)
            curCount = 0
            mem = []
            while maxHq and (n + 1) - curCount > 0:
                v = heapq.heappop(maxHq) + 1
                curCount += 1
                interval += 1
                if v < 0:
                    mem.append(v)

            maxHq += mem
            diff = (n + 1) - curCount
            if maxHq and diff > 0:
                interval += diff

            heapq.heapify(maxHq)

        return interval

# @lc code=end

