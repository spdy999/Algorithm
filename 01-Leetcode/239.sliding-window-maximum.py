#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # Monotonic q decreasing 
        n = len(nums)
        res = []
        l = 0

        for r in range(n): # O(n)
            while q and nums[q[-1]] < nums[r]: # keep monotonic decreasing q
                q.pop()

            if q and (r + 1) >= k and l > q[0] : # pop out of window
                q.popleft()

            q.append(r)

            if (r + 1) >= k: # moving window and collect maximum in q for the answer
                res.append(nums[q[0]])
                l += 1
        
        return res

        # bigO = O(n)lution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
# @lc code=end

