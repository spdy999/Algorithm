#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            guessed = guess(mid)
            if guessed == 0: # found
                return mid
            elif guessed == 1: # on the right
                l = mid + 1
            elif guessed == -1: # on the left
                r = mid - 1

        
# @lc code=end

