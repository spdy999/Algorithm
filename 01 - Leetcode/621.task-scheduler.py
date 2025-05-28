#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Time: O(n log n)
        # Space: O(n)
        cnt = Counter(tasks) # O(n)
        interval = 0
        maxHq = [(-v,c) for c, v in cnt.items()] # O(n)
        heapq.heapify(maxHq) # O(log n)
        q = deque() # [(freq, interval, c)]

        while maxHq or q: # O(n)
            interval += 1
            # print('interval:', interval)
            # print('maxHq:', maxHq)
            # print('q:', q)
            # print()
            if maxHq:
                freq, c = heapq.heappop(maxHq) # O(log n)
                freq += 1
                if freq: # if freq is not 0
                    q.append((freq, interval + n, c))
            
            if q and q[0][1] == interval:
                freq, i, c = q.popleft()
                heapq.heappush(maxHq, (freq, c)) # O(log n)

        return interval

# @lc code=end

