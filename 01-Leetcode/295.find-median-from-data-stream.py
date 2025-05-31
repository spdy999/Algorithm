#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
class MedianFinder:

    def __init__(self):
        self.left = [] # maxHq
        self.right = [] # minHq

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        # len diff need to be only 0 or 1
        # left[0] < right[0]
        while abs(len(self.left) - len(self.right)) > 1 or \
         ((self.left and self.right) and -self.left[0] > self.right[0]):
            if len(self.left) > len(self.right):
                heapq.heappush(self.right, -heapq.heappop(self.left))
            else:
                heapq.heappush(self.left, -heapq.heappop(self.right))
        # print('addNum left, right:', sorted(self.left), sorted(self.right))

    def findMedian(self) -> float:
        lenL = len(self.left)
        lenR = len(self.right)

        if lenL > lenR:
            return -self.left[0]
        elif lenL < lenR:
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

