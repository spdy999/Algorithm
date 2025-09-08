#
# @lc app=leetcode id=480 lang=python3
#
# [480] Sliding Window Median
#

# @lc code=start
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        maxHeap = []
        minHeap = []
        heapDict = collections.defaultdict(int)
        res = []

        def balance():
            print(nums[i])
            print('before balance:')
            print('maxHeap:', [-x for x in maxHeap])
            print('minHeap:', minHeap)
            balance = -1 if prevNum <= med else 1 # -1 => prev is in L(maxHq), +1 => prev is in R(minHq)

            if nums[i] <= med:
                balance += 1
                heapq.heappush(maxHeap, -nums[i])
            else:
                balance -= 1
                heapq.heappush(minHeap, nums[i])
            

            if balance < 0: # maxHeap is too less; not balance
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))
            elif balance > 0: # minHeap is too less; not balance
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))

            while maxHeap and heapDict[-maxHeap[0]] > 0:
                heapDict[-maxHeap[0]] -= 1
                heapq.heappop(maxHeap)
            
            while minHeap and heapDict[minHeap[0]] > 0:
                heapDict[minHeap[0]] -= 1
                heapq.heappop(minHeap)
            print()
            print('after balance:')
            print('balance:', balance)
            print('maxHeap:', [-x for x in maxHeap])
            print('minHeap:', minHeap)
            print('----')
        for i in range(k):
            heapq.heappush(maxHeap, -nums[i])
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))

            if len(minHeap) > len(maxHeap):
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))
            
        
        med = None
        if k%2 == 1:
            med = -maxHeap[0]
            res.append(med)
        else:
            med = (-maxHeap[0] + minHeap[0]) / 2
            res.append(med)

        for i in range(k, len(nums)):
            prevNum = nums[i - k]
            heapDict[prevNum] += 1
            # balance heap:
            # 1. len(maxHeap) = len(minHeap)
            # 2. diff between maxHeap and minHeap = 1
            # so, balance < 0 ==> L(maxHq) < R(minHq)
            balance()


            if k%2 == 1:
                med = -maxHeap[0]
                res.append(med)
            else:
                med = (-maxHeap[0] + minHeap[0]) / 2
                res.append(med)
            
        return res

        
# @lc code=end

