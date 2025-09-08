#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#

# @lc code=start
class TreeNode:
    def __init__(self, start: int, end: int):
        self.left = None
        self.right = None
        self.start = start
        self.end = end

    def insert(self, startTime: int, endTime: int):
        cur = self
        while True:
            if cur.end <= startTime: # insert to right (after)
                if cur.right is None:
                    cur.right = TreeNode(startTime, endTime)
                    return True
                cur = cur.right
            elif endTime <= cur.start: # insert to left (before)
                if cur.left is None:
                    cur.left = TreeNode(startTime, endTime)
                    return True
                cur = cur.left
            else:
                return False


class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        if self.root is None:
            self.root = TreeNode(startTime, endTime)
            return True

        return self.root.insert(startTime, endTime)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
# @lc code=end

